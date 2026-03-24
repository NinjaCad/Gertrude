from testing_base import *

def test_counter_increment():
    players = ["Daniel", "Joseph", "Rose", "Faith", "Eli", "David"] 
    game_state = {'counter': 0}
    
    rank, player_turn = blank(game_state, players)

    assert rank == 1
    assert player_turn == 1
    assert players[player_turn] == "Joseph"

def test_counter_loop_through_players():
    players = ["Daniel", "Joseph", "Rose", "Faith", "Eli", "David"] 
    game_state = {'counter': 0}

    for i in range(6):
        rank, player_turn = blank(game_state, players)

    assert rank == 6
    assert player_turn == 0
    assert players[player_turn] == "Daniel"

def test_counter_loop_through_ranks():
    players = ["Daniel", "Joseph", "Rose", "Faith", "Eli", "David"] 
    game_state = {'counter': 0}

    for i in range(13):
        rank, player_turn = blank(game_state, players)

    # current_count is 13. 13 % 13 == 0. 13 % 6 == 1.
    assert rank == 0
    assert player_turn == 1
    assert players[player_turn] == "Joseph"
