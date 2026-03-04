from cardgames.Deck import Deck
from cardgames.Player import Player


def hit_test():
    
    # Test 1: Deck when it is empty tries hit
    deck_empty = Deck()
    deck_empty.cards = []
    deck_empty.size = 0

    player1 = Player("testPlayer1")

    test1 = player1.hit(deck_empty)

    if test1 is None:
        print("Deck Empty")
    else:
        print("Deck still has Cards")

    # Test 2: Deck when it has cards
    deck_full = Deck()
    deck_full.shuffle()

    player2 = Player("testPlayer2")

    test2 = player2.hit(deck_full)

    if test2 is not None and len(player2.hand) == 1:
        print("Card Drawn succesfully")
    else: 
        print("Test Failed")

hit_test()
# test for if() and test for else() by calling hit function and inputing a card value from the deck and seeing if it runs the function succesfully