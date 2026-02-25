from testing_base import *


def test_3player():
    game = Games()

    players = ["dory", "marvin", "nemo"] #Test Players

    player1 = game.rand_start(players)
    assert player1 != None
    print("Player1 Exists")
    assert isinstance(player1, Player) == True
    print("Player1 is type Player")
