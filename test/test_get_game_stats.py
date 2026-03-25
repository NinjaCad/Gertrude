from testing_base import *

game = Games()

previous_game_stats = {"Player1": {"Wins": 1, "Win-Rate": "33.3%"},
                  "Player2": {"Wins": 2, "Win-Rate": "66.7%"},
                  "Ties": 0 }

new_game_stats = {"Player1": {"Wins": 2, "Win-Rate": "50.0%"},
                  "Player2": {"Wins": 2, "Win-Rate": "50.0%"},
                  "Ties": 0 }

tie_game_stats = {"Player1": {"Wins": 1, "Win-Rate": "25.0%"},
                  "Player2": {"Wins": 2, "Win-Rate": "50.0%"},
                  "Ties": 1 }

players = ["Player1", "Player2"]
players_2 = ["Player2", "Player3"]

def test_game_stats():
    #This should pass
    game_stats = game.get_game_stats("Player1", players, previous_game_stats)
    assert game_stats["Player1"]["Wins"] == new_game_stats["Player1"]["Wins"]
    assert game_stats["Player2"]["Wins"] == new_game_stats["Player2"]["Wins"]
    assert game_stats["Player1"]["Win-Rate"] == new_game_stats["Player1"]["Win-Rate"]
    assert game_stats["Player2"]["Win-Rate"] == new_game_stats["Player2"]["Win-Rate"]
    assert game_stats["Ties"] == new_game_stats["Ties"]

def test_winner_not_in_dict():
    #This should fail
    game_stats = game.get_game_stats("Player3", players, previous_game_stats)
    assert game_stats["Player1"]["Wins"] == new_game_stats["Player1"]["Wins"]
    assert game_stats["Player2"]["Wins"] == new_game_stats["Player2"]["Wins"]
    assert game_stats["Player1"]["Win-Rate"] == new_game_stats["Player1"]["Win-Rate"]
    assert game_stats["Player2"]["Win-Rate"] == new_game_stats["Player2"]["Win-Rate"]
    assert game_stats["Ties"] == new_game_stats["Ties"]

def test_invalid_winner_with_no_dict_passed():
    #This should fail
    game_stats = game.get_game_stats("Player3", players)
    assert game_stats["Player1"]["Wins"] == new_game_stats["Player1"]["Wins"]
    assert game_stats["Player2"]["Wins"] == new_game_stats["Player2"]["Wins"]
    assert game_stats["Player1"]["Win-Rate"] == new_game_stats["Player1"]["Win-Rate"]
    assert game_stats["Player2"]["Win-Rate"] == new_game_stats["Player2"]["Win-Rate"]
    assert game_stats["Ties"] == new_game_stats["Ties"]

def test_player_not_in_dict():
    #This should fail
    game_stats = game.get_game_stats("Player1", players_2, previous_game_stats)
    assert game_stats["Player1"]["Wins"] == new_game_stats["Player1"]["Wins"]
    assert game_stats["Player2"]["Wins"] == new_game_stats["Player2"]["Wins"]
    assert game_stats["Player1"]["Win-Rate"] == new_game_stats["Player1"]["Win-Rate"]
    assert game_stats["Player2"]["Win-Rate"] == new_game_stats["Player2"]["Win-Rate"]
    assert game_stats["Ties"] == new_game_stats["Ties"]

def test_tie():
    #This should pass
    game_stats = game.get_game_stats("It's a tie!", players, previous_game_stats)
    assert game_stats["Player1"]["Wins"] == tie_game_stats["Player1"]["Wins"]
    assert game_stats["Player2"]["Wins"] == tie_game_stats["Player2"]["Wins"]
    assert game_stats["Player1"]["Win-Rate"] == tie_game_stats["Player1"]["Win-Rate"]
    assert game_stats["Player2"]["Win-Rate"] == tie_game_stats["Player2"]["Win-Rate"]
    assert game_stats["Ties"] == tie_game_stats["Ties"]

def test_no_dict_passed():
    #This should fail
    game_stats = game.get_game_stats("Player1", players)
    assert game_stats["Player1"]["Wins"] == new_game_stats["Player1"]["Wins"]
    assert game_stats["Player2"]["Wins"] == new_game_stats["Player2"]["Wins"]
    assert game_stats["Player1"]["Win-Rate"] == new_game_stats["Player1"]["Win-Rate"]
    assert game_stats["Player2"]["Win-Rate"] == new_game_stats["Player2"]["Win-Rate"]
    assert game_stats["Ties"] == new_game_stats["Ties"]