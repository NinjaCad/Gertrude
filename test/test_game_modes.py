# test_gamemodes.py
from cardgames.Game_modes import Games

def test_setup_gamemode_two_players():
    # simulate inputs: 2 players, 3 cards, 5 rounds
    inputs = iter(["2", "3", "5"])
    game = Games(input_func=lambda _: next(inputs))
    rounds, pool_size = game.setup_gamemode()

    assert len(game.players) == 2
    assert rounds == 5
    assert pool_size == 3

def test_setup_gamemode_one_player():
    # simulate inputs: 1 player, 4 cards, 3 rounds
    inputs = iter(["1", "4", "3"])
    game = Games(input_func=lambda _: next(inputs))
    rounds, pool_size = game.setup_gamemode()

    assert len(game.players) == 1
    assert rounds == 3
    assert pool_size == 4

def test_setup_gamemode_max_cards():
    # simulate inputs: 3 players, 5 cards, 7 rounds
    inputs = iter(["3", "5", "7"])
    game = Games(input_func=lambda _: next(inputs))
    rounds, pool_size = game.setup_gamemode()

    assert len(game.players) == 3
    assert rounds == 7
    assert pool_size == 5