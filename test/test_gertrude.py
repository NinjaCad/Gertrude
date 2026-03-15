from testing_base import *

def test_playerGertrude():
    deck = Deck()
    dlr = Dealer(deck)
    gert = Gertrude("Gertrude")
    hand = [getCard("Spades", 1), getCard("Diamonds", 14)]
    gert.setHand(hand) 
    score = gert.gertTurn(dlr)
    assert score == 21

def test_playGert():
    deck2 = Deck()
    delr = Dealer(deck2)
    gert2 = Gertrude("Gertrude")
    hand = [getCard("Spades", 1), getCard("Diamonds", 14)]
    gert2.setHand(hand)
    sc = gert2.gertTurn(delr)
    assert sc >= 17