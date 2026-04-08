from testing_base import *

game = Games()

game_stats_1 = {"Player1": {"Wins": 1, "Win-Rate": "100.0%", "Win Streak": 1, "Highest Win Streak": 1},
                  "Player2": {"Wins": 0, "Win-Rate": "0.0%", "Win Streak": 0, "Highest Win Streak": 0},
                  "Ties": 0 }


previous_game_stats = {"Player1": {"Wins": 1, "Win-Rate": "33.3%", "Win Streak": 0, "Highest Win Streak": 1},
                  "Player2": {"Wins": 2, "Win-Rate": "66.7%", "Win Streak": 1, "Highest Win Streak": 1},
                  "Ties": 0 }

new_game_stats = {"Player1": {"Wins": 2, "Win-Rate": "50.0%", "Win Streak": 1, "Highest Win Streak": 1},
                  "Player2": {"Wins": 2, "Win-Rate": "50.0%", "Win Streak": 0, "Highest Win Streak": 1},
                  "Ties": 0 }

tie_game_stats = {"Player1": {"Wins": 1, "Win-Rate": "25.0%", "Win Streak": 0, "Highest Win Streak": 1},
                  "Player2": {"Wins": 2, "Win-Rate": "50.0%", "Win Streak": 0, "Highest Win Streak": 1},
                  "Ties": 1 }

players = ["Player1", "Player2"]

def test_win_streak_with_no_dict_passed():
    game_stats = game.get_game_stats("Player1", players)
    assert game_stats["Player1"]["Win Streak"] == game_stats_1["Player1"]["Win Streak"]
    assert game_stats["Player2"]["Win Streak"] == game_stats_1["Player2"]["Win Streak"]
    assert game_stats["Player1"]["Highest Win Streak"] == game_stats_1["Player1"]["Highest Win Streak"]
    assert game_stats["Player2"]["Highest Win Streak"] == game_stats_1["Player2"]["Highest Win Streak"]

def test_player1_win_streak_with_dict_passed():
    game_stats = game.get_game_stats("Player1", players, previous_game_stats)
    assert game_stats["Player1"]["Win Streak"] == new_game_stats["Player1"]["Win Streak"]
    assert game_stats["Player2"]["Win Streak"] == new_game_stats["Player2"]["Win Streak"]
    assert game_stats["Player1"]["Highest Win Streak"] == new_game_stats["Player1"]["Highest Win Streak"]
    assert game_stats["Player2"]["Highest Win Streak"] == new_game_stats["Player2"]["Highest Win Streak"]

def test_tie_win_streak():
    game_stats = game.get_game_stats("It's a tie!", players, previous_game_stats)
    assert game_stats["Player1"]["Win Streak"] == tie_game_stats["Player1"]["Win Streak"]
    assert game_stats["Player2"]["Win Streak"] == tie_game_stats["Player2"]["Win Streak"]
    assert game_stats["Player1"]["Highest Win Streak"] == tie_game_stats["Player1"]["Highest Win Streak"]
    assert game_stats["Player2"]["Highest Win Streak"] == tie_game_stats["Player2"]["Highest Win Streak"]
#-----------------------------------------------------------------------------------------------------------
#game_stats_1 is input, win order: P1, P1
game_stats_2 = {"Player1": {"Wins": 2, "Win-Rate": "100.0%", "Win Streak": 2, "Highest Win Streak": 2},
                  "Player2": {"Wins": 0, "Win-Rate": "0.0%", "Win Streak": 0, "Highest Win Streak": 0},
                  "Ties": 0 }

def test_increment_highest_win_streak():
    game_stats = game.get_game_stats("Player1", players, game_stats_1)
    assert game_stats["Player1"]["Highest Win Streak"] == game_stats_2["Player1"]["Highest Win Streak"]
    assert game_stats["Player2"]["Highest Win Streak"] == game_stats_2["Player2"]["Highest Win Streak"]

#------------------------------------------------------------------------------------------------------------
#game_stats_1 is input, win order: P1, P2
game_stats_3 = {"Player1": {"Wins": 1, "Win-Rate": "50.0%", "Win Streak": 0, "Highest Win Streak": 1},
                  "Player2": {"Wins": 1, "Win-Rate": "50.0%", "Win Streak": 1, "Highest Win Streak": 1},
                  "Ties": 0 }

def test_highest_win_streak_update_other_player():
    game_stats = game.get_game_stats("Player2", players, game_stats_1)
    assert game_stats["Player1"]["Highest Win Streak"] == game_stats_3["Player1"]["Highest Win Streak"]
    assert game_stats["Player2"]["Highest Win Streak"] == game_stats_3["Player2"]["Highest Win Streak"]
    
#------------------------------------------------------------------------------------------------------
#Win Order: P1, P1, P2
game_stats_4_input = {"Player1": {"Wins": 2, "Win-Rate": "66.6%", "Win Streak": 0, "Highest Win Streak": 2},
                  "Player2": {"Wins": 1, "Win-Rate": "33.3%", "Win Streak": 1, "Highest Win Streak": 1},
                  "Ties": 0}

#Win Order: P1, P1, P2, P1
game_stats_4 = {"Player1": {"Wins": 3, "Win-Rate": "75.0%", "Win Streak": 1, "Highest Win Streak": 2},
                  "Player2": {"Wins": 1, "Win-Rate": "25.0%", "Win Streak": 0, "Highest Win Streak": 1},
                  "Ties": 0 }

def test_highest_win_streak_if_win_streak_less_than_HWS():
    game_stats = game.get_game_stats("Player1", players, game_stats_4_input)
    assert game_stats["Player1"]["Highest Win Streak"] == game_stats_4["Player1"]["Highest Win Streak"]
    assert game_stats["Player2"]["Highest Win Streak"] == game_stats_4["Player2"]["Highest Win Streak"]
  