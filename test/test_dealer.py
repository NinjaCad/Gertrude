from testing_base import *


deck = Deck() 
dealer = Dealer(deck)
pl1 = Player('Player1')
pl2 = Player('Player2')
pl3 = Player('Player3')

def test_deal_cards_big():
    #this function tests the 'if' statement in dealcards()
    #by seeing if it will deal cards when there are too many
    #players and cards
    playerList = [pl1, pl2, pl3] * 9
    assert dealer.dealCards(2, playerList) == False

def test_deal_cards_amount():
    playerList = [pl1, pl2, pl3]
    dealer.dealCards(2, playerList)
    for i in range(len(playerList)):
        print(playerList[i].knownCards)
        assert len(playerList[i].knownCards) == 2

    