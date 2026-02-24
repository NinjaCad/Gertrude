from testing_base import *

# This is just a template.

# test function 
def test_addCard():
    # initialize test deck
    test_deck = Deck()
    # 5 cards from the deck for the hand
    # test_dealt_hand = [test_deck.cards[0], test_deck.cards[12], test_deck.cards[26], test_deck.cards[35], test_deck.cards[4]]

    # initialize test player
    test_player = Player("Player1_Tester")

    # call setHand function passing in test hand
    test_player.setHand(test_dealt_hand)

    # compare the test hand against the expected length
    assert len(test_player.hand) == 5
    # compare the test hand against the expected knownCards list
    assert len(test_player.knownCards) == 0

    # Outputs the test hand for visual confirmation
    for card in test_dealt_hand:
        print(card)

    # here's my test command: "pytest test_player-set_hand.py -rA --capture=tee-sys --html=set_hand_report.html --self-contained-html"
        # modifiers: -rA to show more detail in terminal; --capture=tee-sys captures output live and displays it in terminal; 
            # --html and --self-contained-html to generate a report of the test results in html format with CSS embedded in the file for portability
