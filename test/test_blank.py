from testing_base import *

def test_counter_increment():
    players = ["Daniel", "Joseph", "Rose", "Faith", "Eli", "David"] 
    game = Games(players)
    rank, player_turn = game.blank()

    assert rank == 1
    assert player_turn == 1
    assert game.player_list[player_turn] == "Joseph"

def test_counter_loop_through_players():
    players = ["Daniel", "Joseph", "Rose", "Faith", "Eli", "David"] 
    game = Games(players)

    for i in range(6):
        rank, player_turn = game.blank()

    assert rank == 6
    assert player_turn == 0
    assert game.player_list[player_turn] == "Daniel"

def test_counter_loop_through_ranks():
    players = ["Daniel", "Joseph", "Rose", "Faith", "Eli", "David"] 
    game = Games(players)

    for i in range(13):
        rank, player_turn = game.blank()

    assert rank == 0
    assert player_turn == 1

