from fastapi.testclient import TestClient

from cardgames.webapp import app


client = TestClient(app)


def _rank_key(label: str) -> tuple[int, int]:
    value_name, suit = label.split(" of ")
    value_map = {
        "Ace": 1,
        "Jack": 11,
        "Queen": 12,
        "King": 13,
    }
    suit_rank = {
        "Spades": 1,
        "Hearts": 2,
        "Diamonds": 3,
        "Clubs": 4,
    }
    if value_name in value_map:
        v = value_map[value_name]
    else:
        v = int(value_name)
    return (v, suit_rank[suit])


def test_create_game_then_play_round_to_completion():
    create_res = client.post(
        "/api/games",
        json={"player1_name": "PlayerX", "player2_name": "PlayerY"},
    )
    assert create_res.status_code == 200

    game = create_res.json()
    assert game["phase"] == "waiting_player1"
    assert len(game["players"]) == 2
    assert len(game["players"][0]["cards"]) == 3
    # During Player 1's turn, Player 2's hand should be hidden in the web view.
    assert all(card["known"] is False for card in game["players"][1]["cards"])
    assert all(card["known"] is True for card in game["players"][0]["cards"])

    game_id = game["game_id"]

    p1_res = client.post(f"/api/games/{game_id}/player1-choice", json={"card_index": 1})
    assert p1_res.status_code == 200
    game = p1_res.json()
    assert game["phase"] == "waiting_player2"
    # During Player 2's turn, Player 1's hand should be hidden in the web view.
    assert all(card["known"] is False for card in game["players"][0]["cards"])
    assert all(card["known"] is True for card in game["players"][1]["cards"])

    p2_res = client.post(f"/api/games/{game_id}/player2-choice", json={"card_index": 2})
    assert p2_res.status_code == 200
    game = p2_res.json()

    assert game["phase"] == "complete"
    assert game["winner"] is not None
    assert game["winner_index"] in (0, 1)
    assert game["players"][0]["cards"][1]["known"] is False
    assert game["players"][0]["chosen_card"] is not None
    assert game["players"][1]["chosen_card"] is not None


def test_unknown_game_returns_404():
    res = client.get("/api/games/not-a-real-id")
    assert res.status_code == 404


def test_instructions_endpoints_return_topics_and_text():
    topics_res = client.get("/api/instructions/topics")
    assert topics_res.status_code == 200
    topics = topics_res.json()["topics"]
    assert "overview" in topics

    overview_res = client.get("/api/instructions/overview")
    assert overview_res.status_code == 200
    assert "HIGH_CARD_DRAW" in overview_res.json()["text"]


def test_stats_reset_endpoint_clears_backend_stats():
    # Create and complete one game so stats are populated.
    game = client.post(
        "/api/games",
        json={"player1_name": "ResetA", "player2_name": "ResetB"},
    ).json()
    gid = game["game_id"]
    client.post(f"/api/games/{gid}/player1-choice", json={"card_index": 0})
    complete = client.post(f"/api/games/{gid}/player2-choice", json={"card_index": 0}).json()
    assert complete.get("backend_stats") is not None

    # Reset backend score/profile stores.
    reset_res = client.post("/api/stats/reset")
    assert reset_res.status_code == 200
    assert reset_res.json().get("ok") is True

    # New game should start with cleared stats for this player pair.
    game2 = client.post(
        "/api/games",
        json={"player1_name": "ResetA", "player2_name": "ResetB"},
    ).json()
    assert game2.get("backend_stats") is None


def test_redraw_tokens_persist_for_repeat_winner_name():
    # Play one round where the likely higher card is chosen for Alpha.
    game = client.post(
        "/api/games",
        json={"player1_name": "Alpha", "player2_name": "Beta"},
    ).json()
    gid = game["game_id"]

    p1_cards = game["players"][0]["cards"]
    p2_cards = game["players"][1]["cards"]

    p1_best = max(p1_cards, key=lambda c: _rank_key(c["label"]))["index"]
    p2_worst = min(p2_cards, key=lambda c: _rank_key(c["label"]))["index"]

    client.post(f"/api/games/{gid}/player1-choice", json={"card_index": p1_best})
    complete = client.post(f"/api/games/{gid}/player2-choice", json={"card_index": p2_worst}).json()
    assert complete.get("backend_stats") is not None

    winner = complete["winner"]

    # Start a new round with same names. Winner from previous round should have >=1 redraw token.
    game2 = client.post(
        "/api/games",
        json={"player1_name": "Alpha", "player2_name": "Beta"},
    ).json()

    p1_tokens = game2["players"][0]["redraw_tokens"]
    p2_tokens = game2["players"][1]["redraw_tokens"]

    if winner == "Alpha":
        assert p1_tokens >= 1
        assert p2_tokens == 0
    elif winner == "Beta":
        assert p2_tokens >= 1
        assert p1_tokens == 0
    else:
        assert p1_tokens == 0
        assert p2_tokens == 0

    # Redraw endpoint should work for current player if that current player has a token.
    # Current player is player1 at start.
    redraw_res = client.post(f"/api/games/{game2['game_id']}/redraw-current")
    if winner == "Alpha":
        assert redraw_res.status_code == 200
        after_redraw = redraw_res.json()
        assert after_redraw["players"][0]["redraw_tokens"] == p1_tokens - 1
    else:
        assert redraw_res.status_code in (400,)
