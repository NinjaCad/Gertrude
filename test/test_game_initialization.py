from testing_base import *
from cardgames.game_initialization import *
from cardgames.Player import Player
import pytest

# From this website: https://stackoverflow.com/questions/60154589/update-and-share-variable-between-tests-on-pytest
@pytest.fixture(scope='module')
def myFixture():
    names = ['Daniel', 'David', 'Eli', 'Faith', 'Joseph', 'Rose']
    num = len(names)
    yield names, num

# Tests that cardsLeft is returned as 52 % 6
def test_create_players_cardsLeft(myFixture):
    names, num = myFixture
    players, cards_left = create_players(num, names)

    assert cards_left == 52 % num

# Tests that players is returned as a list and as long as the number of names given
def test_create_players_list_and_len(myFixture):
    names, num = myFixture
    players, cards_left = create_players(num, names)

    assert isinstance(players, list)
    assert len(players) == num

# Tests that inputted player names are the names of the Player objects
def test_create_players_names(myFixture):
    names, num = myFixture
    players, cards_left = create_players(num, names)

    player_names = [p.name for p in players]
    for name in names:
        assert name in player_names

# Tests that each Player object's angle is valid:
# -unique
# -between 0 and 360
# -a multiple of 60 (because 6 players were passed in, 360/6 = 60) 
def test_create_players_angles(myFixture):
    names, num = myFixture
    players, cards_left = create_players(num, names)
    angles = [p.angle for p in players]
    # unique
    assert len(set(angles)) == num 
    angle_offset = 360 / num
    for angle in angles:
        # within the limits of a circle
        assert 0 <= angle < 360
        # multiple of 360/6 = 60
        assert angle % angle_offset == 0

# Tests appropriate error messages are outputted for bad input
# Tests for correct storage of input
def test_start_game_inputs(monkeypatch, capfd):
    # Source - https://stackoverflow.com/a/59998012
    # Posted by theY4Kman
    # Retrieved 2026-02-24, License - CC BY-SA 4.0
    responses = iter([0, 'f', 6, 'Daniel', 'David', 'Eli', 'Faith', 'Joseph', 'Rose'])
    monkeypatch.setattr('builtins.input', lambda msg: next(responses))
    
    # Run the function
    player_names, num_players = start_game()
    
    # Source - https://stackoverflow.com/a/20507769
    # Posted by James Mills, modified by community. See post 'Timeline' for change history
    # Retrieved 2026-02-24, License - CC BY-SA 4.0
    out, err = capfd.readouterr()
    assert "Welcome to HEART ATTACK!" in out
    assert "You need at least 2 players." in out
    assert "That's not a valid number." in out
    assert player_names == ['Daniel', 'David', 'Eli', 'Faith', 'Joseph', 'Rose']
    assert num_players == 6