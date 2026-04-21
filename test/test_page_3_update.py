
from testing_base import *

import pytest
from cardgames.Games import app, GAME_STATE, player_list
from cardgames.Player import Player
from cardgames.Deck import Deck
from cardgames.Card import Card


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def auth_client(client):
    with client.session_transaction() as game_session:
        game_session["name"] = "test_player_1"
    return client

@pytest.fixture
def setup_game():
    global GAME_STATE, player_list
    GAME_STATE.clear()

    GAME_STATE.update({
        "current_card": None,
        "current_art": "",
        "match_rank": 1,
        "current_player": None,
        "played_cards": [],
        "slap_list": [],
        "slap_in_progress": False,
        "counter": 0,
        "game_started": False
    })
    
    player_list.clear()
    player_list.extend([
        Player("test_player_1"),
        Player("test_player_2"),
        Player("test_player_3"),
    ])
    

def test_bad_slap(auth_client, setup_game):

    card = Card("Hearts", 5, [], [])
    GAME_STATE["current_card"] = card
    GAME_STATE["match_rank"] = 3
    GAME_STATE["played_cards"] = [card]
    GAME_STATE["current_player"] = player_list[0]
    
    response = auth_client.post("/slap", data={"timestamp": "0"})

    assert response.status_code == 204
    assert len(player_list[0].hand) > 0

def test_good_slap(auth_client, setup_game):

    card = Card("Hearts", 5, [], [])
    GAME_STATE["current_card"] = card
    GAME_STATE["match_rank"] = 5
    GAME_STATE["played_cards"] = [card]
    GAME_STATE["current_player"] = player_list[0]

    response = auth_client.post("/slap", data={"timestamp": "0"})

    assert response.status_code == 204
    assert GAME_STATE["slap_in_progress"] is True


def test_game_route_initializes_game(auth_client, setup_game):
            
    response = auth_client.get("/game")

    assert response.status_code == 200
    assert GAME_STATE["game_started"] is True

def test_lock_play_button_for_others(client, setup_game):
    
    with client.session_transaction() as game_session:
        game_session["name"] = "test_player_2"

    GAME_STATE["current_player"] = player_list[0]
    GAME_STATE["game_started"] = True

    response = client.post("/game")

    assert response.status_code == 302



