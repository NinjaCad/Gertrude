from cardgames.Deck import Deck
from cardgames.Dealer import Dealer
from cardgames.Player import Player

def test_dealCards():
    deck = Deck()
    dealer = Dealer(deck)

    players = [Player("p1"), Player("p2")]

    success = dealer.dealCards(players)

    assert success is True
    for player in players:
        assert len(player.hand) == 3

def test_dealCards_Limit():  #Tests to see if dealer fails if out of cards
    deck = Deck()
    dealer = Dealer(deck)

    players = [Player("P1") for _ in range(20)]  # too many players

    success = dealer.dealCards(players)

    assert success is False