from testing_base import *
import random

def test_printHand_basic():
    game = Games()
    players = [Player('1'), Player('2'), Player('3'), Player('4')]
    deck = Deck()
    dealer = Dealer(deck)
    dealer.dealCards(10, players)
    
    # Tests to ensure function prints the back of every players cards except the active player
    for player in players:
        player.isTurn = True
        print(f'######\nPrinting all hands except for {player.name}\'s\n')
        game.showOpponentsHands(players)
        player.isTurn = False

def test_printHand_random():
    game = Games()
    players = [Player('1'), Player('2'), Player('3'), Player('4')]
    deck = Deck()
    deck.shuffle()

    # Tests to ensure function can print different amount of cards
    for player in players:
        for i in range(random.randint(1,12)):
            player.addCard(deck.getCard())

    print(f'Printing {player.name}\'s cards:\n')
    game.showOpponentsHands(players)

def test_printHand_consistency():
    game = Games()
    players = [Player('1')]
    deck = Deck()
    dealer = Dealer(deck)
    dealer.dealCards(10, players)

    #Tests that all modified variables are consistent before and after execution
    beforeHand = players[0].hand
    beforeKnownCards = players[0].knownCards

    game.showOpponentsHands(players)
    assert players[0].hand == beforeHand
    assert players[0].knownCards == beforeKnownCards

if __name__ == "__main__":
    test_printHand_basic()
    test_printHand_random()
    test_printHand_consistency()