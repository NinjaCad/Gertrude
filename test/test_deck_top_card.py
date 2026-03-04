from testing_base import *


def test_get_card_returns_top_card_and_updates_state():
    deck = Deck()

    # top of deck is the last element because getCard() uses list.pop()
    expected_top = deck.cards[-1]

    drawn = deck.getCard()

    assert drawn == expected_top
    assert drawn in deck.discarded
    assert len(deck.cards) == 51
    assert len(deck.discarded) == 1
