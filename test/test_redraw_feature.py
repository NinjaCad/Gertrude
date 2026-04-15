import pytest

from cardgames.Deck import Deck
from cardgames.Dealer import Dealer
from cardgames.Player import Player


def test_redraw_consumes_token_and_deals_three():
    deck = Deck()
    dealer = Dealer(deck)
    player = Player("p1")
    player.add_redraw_token()

    initial_size = deck.size

    success = dealer.redraw_three_card_options(player)

    assert success is True
    assert len(player.hand) == 3
    assert player.redraw_tokens == 0
    assert deck.size == initial_size - 3
    assert len(deck.discarded) == 3


def test_redraw_fails_without_token():
    deck = Deck()
    dealer = Dealer(deck)
    player = Player("p1")

    success = dealer.redraw_three_card_options(player)

    assert success is False
    assert player.hand == []
    assert deck.size == 52
    assert len(deck.discarded) == 0


def test_redraw_refills_deck_when_low():
    deck = Deck()
    dealer = Dealer(deck)
    player = Player("p1")
    player.add_redraw_token()

    # Move a few cards to the discard pile and leave only 2 cards in the deck.
    for _ in range(5):
        deck.getCard()
    deck.cards = deck.cards[:2]
    deck.size = len(deck.cards)

    success = dealer.redraw_three_card_options(player)

    assert success is True
    assert len(player.hand) == 3
    assert deck.size == 4  # 2 original cards + 5 discarded = 7, minus 3 dealt = 4 remain
    assert len(deck.discarded) == 3
