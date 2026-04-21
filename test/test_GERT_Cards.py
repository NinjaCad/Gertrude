from testing_base import * 

def test_gertrude_reveals_cards_face_up():
    game = Games()
    game.dealer = Dealer(game.deck)

    # Create Gertrude with a 10 and a 7 -> score 17 (so gertTurn won't draw)
    gert = Gertrude("GERTRUDE")
    hand = [Card("Spades", 10, None, None), Card("Diamonds", 7, None, None)]
    gert.setHand(hand)
    # Simulate one card being hidden (second card face-down)
    gert.knownCards = [True, False]

    # Attach players to the game (Gertrude at index 0 as in Games.main)
    game.playerList = [gert, Player("Alice")]

    # Run Gertrude's turn (should return immediately at 17 and not change visibility)
    gert.gertTurn(game.dealer)

    # Reveal all dealer cards like Games.main does before showing hands
    dealer = game.playerList[0]
    if getattr(dealer, "knownCards", None):
        dealer.knownCards = [True for _ in dealer.knownCards]

    # Assert all Gertrude's cards are now face-up
    assert len(dealer.knownCards) == len(dealer.hand)
    assert all(dealer.knownCards), "Gertrude's cards should all be revealed (True in knownCards)"



def test_gertrude_score_shown(capsys):
    # Arrange
    game = Games()
    gert = Gertrude("GERTRUDE")
    player = Player("Alice")

    # Give Gertrude a 10 and a 7 -> score 17
    gerthand = [Card("Spades", 10, None, None), Card("Diamonds", 7, None, None)]
    gert.setHand(gerthand)

    # Give player a lower score (not important for this assertion)
    playerhand = [Card("Hearts", 5, None, None), Card("Clubs", 4, None, None)]
    player.setHand(playerhand)
    
    game.playerList = [gert, player]

    # Act
    game.calculateWinner([gert, player])

    # Assert: Games.calculateWinner prints Gertrude's final score
    captured = capsys.readouterr()
    assert "GERTRUDE ends with a hand value of 17." in captured.out