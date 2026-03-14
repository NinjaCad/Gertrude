from testing_base import *

def test_basic():
    game = Games()
    Dory = Player("Dory")
    Marlin = Player("Marlin")
    Nemo = Player("Nemo")
    FishThatAteNemosFamily = Player("ThatGuy")

    players = [Marlin, Dory, Nemo, FishThatAteNemosFamily]
    turn_list = game.card_thievery(players, Dory)