from testing_base import *

def test_playerGertrude(): 
    #this test ensures Gertrude doesn't hit when her score is >= 17
    deck = Deck()
    
    dlr1 = Dealer(deck)
    gert = Gertrude("Gertrude")
    hand = [Card("Spades", 0, None, None), Card("Diamonds", 12, None, None)]
    
    
    gert.setHand(hand) 
    score1 = gert.gertTurn(dlr1)
    assert score1 == 21


def test_playGert():
    #tests that gertrude will hit until her score is >= 17
    deck2 = Deck()
    dlr2 = Dealer(deck2)
    gert2 = Gertrude("Gertrude")
    hand = [Card("Spades", 1, None, None), Card("Diamonds", 14, None, None)]
    gert2.setHand(hand)
    score2 = gert2.gertTurn(dlr2)
    assert score2 >= 17

def test_playerGertrude2():
    #checks that gertrude won't hit on 17, added in after submitting assignment in Canvas
    deck3 = Deck()
    dlr3 = Dealer(deck3)
    gert3 = Gertrude("Gertrude")
    hand = [Card("Spades", 0, None, None), Card("Diamonds", 5, None, None)]
    gert3.setHand(hand)
    score3 = gert3.gertTurn(dlr3)
    assert score3 == 17