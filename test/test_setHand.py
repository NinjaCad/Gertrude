from testing_base import *

# test functions
def test_setHand_handLen():
    # test setHand function ability to have correct len for hand

    # initialize test deck
    test_deck = Deck()
    # 5 cards from the deck for the hand
    test_dealt_hand = [test_deck.cards[0], test_deck.cards[12], test_deck.cards[26], test_deck.cards[35], test_deck.cards[4]]

    # initialize test player
    test_player1 = Player("Eli")
    # call setHand function passing in test hand
    test_player1.set_hand(test_dealt_hand)
    # compare the test hand against the expected length
    assert len(test_player1.hand) == 5

def test_setHand_specific():
    # test setHand function ability to set specific cards

    # initialize test deck
    test_deck = Deck()
    # 5 cards from the deck for the hand
    test_dealt_hand = [test_deck.cards[0], test_deck.cards[12], test_deck.cards[26], test_deck.cards[35], test_deck.cards[4]]

    # initialize test player
    test_player1 = Player("Joseph")
    # call setHand function passing in test hand
    test_player1.set_hand(test_dealt_hand)
    # compare the test hand against the expected knownCards list
    assert test_player1.hand == [test_deck.cards[0], test_deck.cards[12], test_deck.cards[26], test_deck.cards[35], test_deck.cards[4]]

def test_setHand_knownCards():
    # test setHand function ability to keep knownCards to zero

    # initialize test deck
    test_deck = Deck()
    # 5 cards from the deck for the hand
    test_dealt_hand = [test_deck.cards[0], test_deck.cards[12], test_deck.cards[26], test_deck.cards[35], test_deck.cards[4]]

    # initialize test player
    test_player1 = Player("Daniel")
    # call setHand function passing in test hand
    test_player1.set_hand(test_dealt_hand)
    # compare the test hand against the expected knownCards list
    assert len(test_player1.known_cards) == 0
 

def test_setHand_empty():
    # test showing player hand is empty

    # 5 cards from the deck for the hand
    test_empty_hand = []
    # initialize test player
    test_player2 = Player("Rose")
    # call setHand function passing in test hand
    test_player2.set_hand(test_empty_hand)
    # compare the test hand against the expected length
    assert len(test_player2.hand) == 0

    # here's my test command: "pytest test_setHand.py -rA --capture=tee-sys --html=setHand_report.html --self-contained-html"
        # modifiers: -rA to show more detail in terminal; --capture=tee-sys captures output live and displays it in terminal; 
            # --html and --self-contained-html to generate a report of the test results in html format with CSS embedded in the file for portability
