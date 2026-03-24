from testing_base import *


def test_1():
    #Verifies 2 cards are dealt to all, and GERTRUDE's visibility rule.
    deck = Deck()
    dealer = Dealer(deck)
    players = [Player("Alice"), Player("Bob"), Player("GERTRUDE")]
    
    assert dealer.dealCards(2, players) is True
    
    for p in players:
        # Check hand size for everyone
        assert len(p.hand) == 2, f"{p.name} should have 2 cards"
        
        # Check visibility logic
        expected_visibility = [True, False] if p.name == "GERTRUDE" else [True, True]
        assert p.knownCards == expected_visibility, f"Visibility mismatch for {p.name}"


def test_2():
    # Test that dealCards returns False if there aren't enough cards to deal.
    deck = Deck()
    dealer = Dealer(deck)
    # create 27 distinct players -> need 54 cards ( > 52 )
    players = [Player(f"Player{i}") for i in range(27)]
    
    success = dealer.dealCards(2, players)
    
    assert success is False

def test_3():
    # Test that dealCards correctly handles the case where there are exactly enough cards to deal.
    deck = Deck()
    dealer = Dealer(deck)
    players = [Player(f"Player{i}") for i in range(26)]  # 26 players -> need 52 cards
    
    success = dealer.dealCards(2, players)
    
    assert success is True
    for player in players:
        assert len(player.hand) == 2
        assert player.knownCards == [True, True]
