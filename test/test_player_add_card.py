from testing_base import *


def test_add_card_appends_to_hand():
    player = Player("Alice")
    card = getCard("spades", 1)
    assert card is not None

    player.addCard(card)

    assert player.hand == [card]


def test_add_card_defaults_to_known_true():
    player = Player("Alice")
    card = getCard("hearts", 10)
    assert card is not None

    player.addCard(card)

    assert player.knownCards == [True]


def test_add_card_can_be_unknown():
    player = Player("Alice")
    card = getCard("clubs", 2)
    assert card is not None

    player.addCard(card, isKnown=False)

    assert player.hand == [card]
    assert player.knownCards == [False]


def test_add_card_multiple_cards_preserves_order_and_known_flags():
    player = Player("Alice")
    c1 = getCard("spades", 13)
    c2 = getCard("diamonds", 3)
    c3 = getCard("hearts", 12)
    assert c1 is not None and c2 is not None and c3 is not None

    player.addCard(c1)                 # default known
    player.addCard(c2, isKnown=False)  # unknown
    player.addCard(c3, isKnown=True)   # known

    assert player.hand == [c1, c2, c3]
    assert player.knownCards == [True, False, True]
