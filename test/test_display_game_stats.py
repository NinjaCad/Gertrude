from testing_base import *

game = Games()

game_stats_1 = {"Player1": {"Wins": 1, "Win-Rate": "33.3%", "Win Streak": 0, "Highest Win Streak": 1},
                  "Player2": {"Wins": 2, "Win-Rate": "66.7%", "Win Streak": 1, "Highest Win Streak": 1},
                  "Ties": 0,
                  "Total Games": 3}

game_stats_2 = {"Player1": {"Wins": 1, "Win-Rate": "100.0%", "Win Streak": 1, "Highest Win Streak": 1},
                  "Player2": {"Wins": 0, "Win-Rate": "0.0%", "Win Streak": 0, "Highest Win Streak": 0},
                  "Ties": 0,
                  "Total Games": 1}

new_game_stats = {"Player1": {"Wins": 2, "Win-Rate": "50.00%", "Win Streak": 1, "Highest Win Streak": 1},
                  "Player2": {"Wins": 2, "Win-Rate": "50.00%", "Win Streak": 0, "Highest Win Streak": 1},
                  "Ties": 0,
                  "Total Games": 4 }

def test_display_game_stats():
    game.display_game_stats(game_stats_1)

def test_display_game_stats_2():
    game.display_game_stats(game_stats_2)

def test_game_stats():
    game_stats = game.get_game_stats("Player1", ["Player1", "Player2"], game_stats_1)
    game.display_game_stats(game_stats)
    assert game_stats["Player1"]["Win-Rate"] == new_game_stats["Player1"]["Win-Rate"]