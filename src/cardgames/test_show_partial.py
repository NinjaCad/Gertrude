# test_show_partial_hand.py
import pytest

# Change this import to your real module path.
# Example: from cardgames.Player import Player
from Player import Player


class DummyCard:
    pass

def test_show_partial_hand_reveals_one_more_card_each_call():
    p = Player("Dealer")

    # start with all hidden
    p.setHand([DummyCard(), DummyCard(), DummyCard()], isKnown=False)
    assert p.knownCards == [False, False, False]
    assert p.knownCardsCount == 0

    p.show_partial_hand()
    assert p.knownCards == [True, False, False]
    assert p.knownCardsCount == 1

    p.show_partial_hand()
    assert p.knownCards == [True, True, False]
    assert p.knownCardsCount == 2

    p.show_partial_hand()
    assert p.knownCards == [True, True, True]
    assert p.knownCardsCount == 3


def test_show_partial_hand_after_all_revealed_does_nothing():
    p = Player("Dealer")
    p.setHand([DummyCard(), DummyCard()], isKnown=False)

    p.show_partial_hand()
    p.show_partial_hand()
    assert p.knownCards == [True, True]
    assert p.knownCardsCount == 2

    # extra call should not change anything
    p.show_partial_hand()
    assert p.knownCards == [True, True]
    assert p.knownCardsCount == 2


def test_setHand_resets_knownCardsCount():
    p = Player("Dealer")
    p.setHand([DummyCard(), DummyCard()], isKnown=False)
    p.show_partial_hand()
    assert p.knownCardsCount == 1

    p.setHand([DummyCard(), DummyCard(), DummyCard()], isKnown=False)
    assert p.knownCardsCount == 0
    assert p.knownCards == [False, False, False]