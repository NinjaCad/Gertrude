from testing_base import *

def test_base():
    # Inputs: 1, ten, ENTER, 1, jack, ENTER
    # Outputs: You should notice the following being printed out:
        # Cards are printed correctly sorted from least to greatest
        # Opponent's hand should show backs
        # Typing 1 should correctly choose the index and pass
        # Typing ten should choose the ten card to steal
        # It should recognize that a card was stolen and a book was made
        # Making the book should allow the user another turn
        # Books should properly print
        # When opponents hand is empty, should draw card
        # Books should be retained and both should be printed

    print("\ntest_base:")
    game = Games()
    deck = Deck()
    turn_list = [Player("Joker"), Player("Morgana")]
    turn_list[0].isTurn = True
    testHands1 = 10
    testHands2 = 11

    # Looks through a deck to find needed cards
    for card in deck.cards:
        if card.value == testHands1 and len(turn_list[0].hand) <= 2:
            turn_list[0].hand.append(card)
            turn_list[0].knownCards.append(True)
        elif card.value == testHands1 and len(turn_list[0].hand) > 2:
            turn_list[1].hand.append(card)
            turn_list[1].knownCards.append(True)

    for card in deck.cards:
            if card.value == testHands2 and len(turn_list[0].hand) <= 5:
                turn_list[0].hand.append(card)
                turn_list[0].knownCards.append(True)
            elif card.value == testHands2 and len(turn_list[0].hand) > 5:
                turn_list[1].hand.append(card)
                turn_list[1].knownCards.append(True)


    turn_list[0].takeTurn(turn_list, game)

def test_handEmpty():
    # Input: nothing
    # Output: player should pick up and be able to continue with that card
    print("\ntest_handEmpty:")
    game = Games()
    deck = Deck()
    turn_list = [Player("Joker"), Player("Morgana")]
    turn_list[1].isTurn = True
    testHands1 = 10

    # Looks through a deck to find needed cards
    for card in deck.cards:
        if card.value == testHands1 and len(turn_list[0].hand) <= 2:
            turn_list[0].hand.append(card)
            turn_list[0].knownCards.append(True)
    
    turn_list[1].takeTurn(turn_list, game)

def test_handAndDeckEmpty():
    # Input: nothing
    # Output: It should state "Morgana's hand and the deck are empty, next player..." and continue to the next test
    print("\ntest_handAndDeckEmpty:")
    game = Games()
    deck = Deck()
    game.deck.cards = []
    turn_list = [Player("Joker"), Player("Morgana")]
    turn_list[1].isTurn = True
    testHands1 = 10

    # Looks through a deck to find needed cards
    for card in deck.cards:
        if card.value == testHands1 and len(turn_list[0].hand) <= 2:
            turn_list[0].hand.append(card)
            turn_list[0].knownCards.append(True)

    turn_list[1].takeTurn(turn_list, game)

def test_bookNotMade():
    # Inputs: 1, ten, ENTER
    # Output: Should allow you to go again without giving a book.
        # Should keep stolen cards in next turn
    print("\ntest_bookNotMade:")
    game = Games()
    deck = Deck()
    turn_list = [Player("Joker"), Player("Morgana")]
    turn_list[0].isTurn = True
    testHands1 = 10

    # Looks through a deck to find needed cards
    for card in deck.cards:
        if card.value == testHands1 and len(turn_list[0].hand) <= 1:
            turn_list[0].hand.append(card)
            turn_list[0].knownCards.append(True)
        elif card.value == testHands1 and len(turn_list[0].hand) > 1 and len(turn_list[1].hand) == 0:
            turn_list[1].hand.append(card)
            turn_list[1].knownCards.append(True)

    turn_list[0].takeTurn(turn_list, game)

def test_drawBook():
    # Inputs: RETURN
    # Output: Should give book after drawing the fourth of a kind of card
        # Should print that the hand and deck are empty and end the turn
    print("\ntest_drawBook:")
    game = Games()
    deck = Deck()
    turn_list = [Player("Joker"), Player("Morgana")]
    turn_list[0].isTurn = True
    testHands1 = 10

    # Looks through a deck to find needed cards, and puts fourth card of kind into deck
    for card in deck.cards:
        if card.value == testHands1 and len(turn_list[0].hand) <= 2:
            turn_list[0].hand.append(card)
            turn_list[0].knownCards.append(True)
        elif card.value == testHands1 and len(turn_list[0].hand) > 2:
            game.deck.cards = [card]
            break

    turn_list[0].takeTurn(turn_list, game)

if __name__ == "__main__":
    test_base()
    test_handEmpty()
    test_handAndDeckEmpty()
    test_bookNotMade()
    test_drawBook()