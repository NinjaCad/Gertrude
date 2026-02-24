from testing_base import *

def basic_test_players():
    game = Games()
    # Basic test: make sure function does not return nothing
    players = game.create_players()
    assert players != None
    assert players != []

def test_input_players():
    game = Games()
    # Test by inputting a random string of letters, should not pass
    # Test by inputting a non-integer number, should not pass
    # Test by inputting any integer other than 2, 3, or 4, should not pass
    # Test by inputting a negative integer, which should pass and remove the negative
    players = game.create_players()
    assert isinstance(len(players), int) == True
    assert len(players) in [2,3,4] == True

def test_player_names():
    game = Games()
    # Test by inputting nothing as a name, should not pass
    # Test by inputting the same name twice, should not pass
    # Test by inputting over 16 characters, should not pass
    # Test by inputting number, should pass
    players = game.create_players()
    player_names = []
    
    # Tests to make sure there are no duplicate names
    for player in players:
        assert player.name not in player_names
        player_names.append(player.name)
