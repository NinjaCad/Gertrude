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
