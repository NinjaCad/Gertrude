from testing_base import *

def test_dealCards():
    deck = Deck()
    dealR = Dealer(deck)
    pl1 = Player('Player1')
    pl2 = Player('Player2')
    playerList = [pl1, pl2]
    dealR.dealCards(2, playerList)
    
    pl1.showHand(True)
    pl2.showHand(True)
    

    