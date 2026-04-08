import pytest
from cardgames.Games import app, player_list, GAME_STATE
from cardgames.Player import Player

# source for using Pytest fixtures: https://docs.pytest.org/en/latest/how-to/fixtures.html
@pytest.fixture
# source for using Flask testing feature: https://flask.palletsprojects.com/en/latest/testing/
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture(autouse=True)
def reset_game_state():
    player_list.clear()
    GAME_STATE["current_card"] = None
    GAME_STATE["current_player"] = None
    GAME_STATE["counter"] = 0

def test_play_card_get(client):
    response = client.get("/play_card")
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert "Current Sequence: " in html
    assert "Current Player: " in html
    assert "No player" in html

def test_play_card_post_noplayers(client):
    response = client.post("/play_card")
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert GAME_STATE["current_player"] is None
    assert GAME_STATE['counter'] == 0
    assert "Current Sequence: None" in html
    assert "Current Player: No player" in html

def test_play_card_post_withplayer(client):
    player_list.append(Player("Alice"))
    
    response = client.post("/play_card")
    html = response.get_data(as_text=True)

    assert response.status_code == 200
    assert GAME_STATE["current_player"] is not None
    assert GAME_STATE['current_player'].name == "Alice"
    assert GAME_STATE['counter'] == 1
    assert "Current Player: Alice" in html

def test_play_card_counter_increments(client):
    player_list.append(Player("Alice"))
    
    client.post("/play_card")  # Alice's turn
    client.post("/play_card")  # Alice's turn again (since she's the only player for testing purposes)

    assert GAME_STATE['counter'] == 2
