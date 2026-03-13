from testing_base import *

gertDeal = Dealer(Deck())
gert = Gertrude("Gertrude", gertDeal)
def test_playerGertrude():
    gertHand = [0, 12] 
    score = gert.playerGertrude(gertHand)
    assert score == 21

def test_playGert():
    gertHand = [0, 0]
    sc = gert.playerGertrude(gertHand)
    assert sc >= 17