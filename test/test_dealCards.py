from testing_base import *

def test_deck_empty():
    deck = Deck()
    dealer = Dealer(deck)
    playerList = [Player("Daniel"), Player("Joseph"), Player("Rose"), Player("Faith"), Player("Eli"), Player("David")]

    dealer.dealCards(playerList)

    assert deck.size == 0

def test_player_hands():
    deck = Deck()
    dealer = Dealer(deck)
    playerList = [Player("Daniel"), Player("Joseph"), Player("Rose"), Player("Faith"), Player("Eli"), Player("David")]

    expectedHandAmount = 52//len(playerList)
    expectedPlayersWithExtra = 52 % len(playerList)

    dealer.dealCards(playerList)

    testVar = True
    playersWithExtra = 0
    for player in playerList:
        if len(player.hand) == expectedHandAmount:
            continue
        elif len(player.hand) == expectedHandAmount + 1:
            playersWithExtra += 1
            continue
        else:
            testVar = False
    if playersWithExtra != expectedPlayersWithExtra:
        testVar = False
    
    assert testVar