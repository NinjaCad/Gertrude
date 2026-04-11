from fastapi.testclient import TestClient

from cardgames.webapp import app


client = TestClient(app)


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
