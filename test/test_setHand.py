from testing_base import *

# test function
def test_setHand():
    # initialize test deck
    test_deck = Deck()
    # 5 cards from the deck for the hand
    test_dealt_hand = [test_deck.cards[0], test_deck.cards[12], test_deck.cards[26], test_deck.cards[35], test_deck.cards[4]]
    test_empty_hand = []

    # initialize test player
    test_player1 = Player("Player1_Tester")
    test_player2 = Player("Player2_Tester")

    # call setHand function passing in test hand
    test_player1.setHand(test_dealt_hand)
    test_player2.setHand(test_empty_hand)

    # compare the test hand against the expected length
    assert len(test_player1.hand) == 5
    # compare the test hand against the expected knownCards list
    assert len(test_player1.knownCards) == 0
    assert test_player1.hand == [test_deck.cards[0], test_deck.cards[12], test_deck.cards[26], test_deck.cards[35], test_deck.cards[4]]


    assert len(test_player2.hand) == 0
    assert len(test_player2.hand) == 0


    # Outputs the test hand for visual confirmation
    # for card in test_player.knownCards:
    #     print(card)

    # here's my test command: "pytest test_setHand.py -rA --capture=tee-sys --html=setHand_report.html --self-contained-html"
        # modifiers: -rA to show more detail in terminal; --capture=tee-sys captures output live and displays it in terminal; 
            # --html and --self-contained-html to generate a report of the test results in html format with CSS embedded in the file for portability
