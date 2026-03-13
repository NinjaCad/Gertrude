from testing_base import *

gert = Gertrude("Gertrude")
def test_playerGertrude():
    gertHand = [0, 12] 
    score = gert.playerGertrude(gertHand)
    assert score == 21

def test_playGert():
    gertHand = [0, 0]
    sc = gert.playerGertrude(gertHand)
    assert sc >= 17