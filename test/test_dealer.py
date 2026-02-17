from testing_base import *

def test_dealCards():
    deck = Deck()
    dealR = Dealer(deck)
    pl1 = Player('Player1')
    pl2 = Player('Player2')
    dealR.dealCards(2, [pl1, pl2])
    print(pl1.showHand())
    print(pl2.showHand())
    

    return 