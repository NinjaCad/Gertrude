from testing_base import *

def basic_test_players():
    game = Games()
    # Basic test: make sure function does not return nothing
    print("This is the basic test")
    players = game.create_players()
    assert players != None
    print("Passed")
    assert players != []
    print("Passed")

def test_input_players():
    game = Games()
    # Test by inputting a random string of letters, should not pass
    # Test by inputting a non-integer number, should not pass
    # Test by inputting any integer other than 2, 3, or 4, should not pass
    # Test by inputting a negative integer, should not pass
    print("This is the input test. Input a random string of letters, a non-integer number, any integer other than 2-4, and a negative integer.")
    players = game.create_players()
    assert isinstance(len(players), int) == True
    print("Passed")
    assert 2 <= len(players) <= 4
    print("Passed")

def test_player_names():
    game = Games()
    # Test by inputting nothing as a name, should not pass
    # Test by inputting the same name twice, should not pass
    # Test by inputting over 16 characters, should not pass
    # Test by inputting number, should pass
    print("This is the player name test. Input nothing, the same name twice, more than 16 characters, and inputting a number.")
    players = game.create_players()
    player_names = []
    
    # Tests to make sure there are no duplicate names
    for player in players:
        assert player.name not in player_names
        print("Passed")
        player_names.append(player.name)

basic_test_players()
test_input_players()
test_player_names()