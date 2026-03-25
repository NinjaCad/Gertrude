from testing_base import *


def test_sort_hand_into_values_groups_cards():
    player = Player("Tim")

    cards = [
        Card("Spades", 12, 0, 0),   # Q
        Card("Hearts", 2, 0, 0),    # 2
        Card("Clubs", 13, 0, 0),    # K
        Card("Diamonds", 3, 0, 0),  # 3
        Card("Clubs", 2, 0, 0),     # 2
    ]
    player.setHand(cards)

    grouped = player.sortHandIntoValues()

    assert list(grouped.keys()) == ["2s", "3s", "Qs", "Ks"]
    assert len(grouped["2s"]) == 2
    assert len(grouped["3s"]) == 1
    assert len(grouped["Qs"]) == 1
    assert len(grouped["Ks"]) == 1
