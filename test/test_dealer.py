from testing_base import *

def test_dealCards():
    deck = Deck()
    dealR = Dealer(deck)
    pl1 = Player('Player1')
    pl2 = Player('Player2')
    pl3 = Player('Player3')
    playerList = [pl1, pl2, pl3] * 9
    assert dealR.dealCards(2, playerList) == False
    
    playerList = [pl1, pl2, pl3]
    dealR.dealCards(2, playerList)
    for i in range(len(playerList)):
        print(playerList[i].knownCards)
        assert len(playerList[i].knownCards) == 2

    