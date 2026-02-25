from testing_base import *


def test_basic():
    game = Games()
    Dory = Player("Dory")

    players = [Dory] #Test Players

    turn_list = game.start_game(players)
    assert isinstance(turn_list, list) == True
    print("turn_list is type List")
    assert isinstance(turn_list[0], Player) == True
    print("player is of type Player")


def test_2player():
    game = Games()
    Dory = Player("Dory")
    Marvin = Player("Marlin")

    players = [Marvin, Dory]

    turn_list = game.start_game(players)
    assert len(turn_list) == 2
    print("Length of list = 2")
    assert len(turn_list[0].hand) == 7
    print("Player has 7 cards in hand")

def test_4player():
    game = Games()
    Dory = Player("Dory")
    Marvin = Player("Marlin")
    Nemo = Player("Nemo")
    FishThatAteNemosFamily = Player("ThatGuy")

    players = [Marvin, Dory, Nemo, FishThatAteNemosFamily]
    turn_list = game.start_game(players)

    assert len(turn_list) == 4
    print("Length of list = 4")
    assert len(turn_list[0].hand) == 5
    print("Player has 5 cards in hand")

test_basic()
test_2player()
test_4player()
