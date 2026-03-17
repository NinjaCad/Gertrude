from testing_base import *


def test_1():
    # Test that dealCards correctly deals 2 cards to each player
    # and that GERTRUDE's second card is hidden.
    deck = Deck()
    dealer = Dealer(deck)
    players = [Player("Alice"), Player("Bob"), Player("GERTRUDE")]
    
    success = dealer.dealCards(2, players)
    
    assert success is True
    assert len(players[0].hand) == 2
    assert len(players[1].hand) == 2
    assert len(players[2].hand) == 2
    assert players[0].knownCards == [True, True]
    assert players[1].knownCards == [True, True]
    assert players[2].knownCards == [True, False]


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

def test_4():
    #test that checks if GERTRUDE's second card is hidden 
    deck = Deck()
    dealer = Dealer(deck)
    players = [Player("Alice"), Player("Bob"), Player("Charlie"), Player("GERTRUDE")] 

    success = dealer.dealCards(2, players)
    assert success is True
    assert len(players[0].hand) == 2
    assert len(players[1].hand) == 2
    assert len(players[2].hand) == 2
    assert len(players[3].hand) == 2
    assert players[0].knownCards == [True, True]
    assert players[1].knownCards == [True, True]
    assert players[2].knownCards == [True, True]
    assert players[3].knownCards == [True, False]   
