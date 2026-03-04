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
    #this function tests that when dealcards() is called
    #and the if statement is not true
    #then the for loop properly assigns the correct
    #amount of cards to each player
    playerList = [pl1, pl2, pl3]
    dealer.dealCards(2, playerList)
    assert len(playerList[0].knownCards) == 2
    assert len(playerList[1].knownCards) == 2
    assert len(playerList[2].knownCards) == 2

    