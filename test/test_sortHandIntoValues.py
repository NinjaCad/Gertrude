from testing_base import *


def test_sortHandIntoValues():
    player = Player("Toby")
    sorted_hand = player.sortHandIntoValues()
    sorted_values = [card.value for card in sorted_hand]

    assert sorted_values == sorted(sorted_values)


def test_groupHandByValues():
    player = Player("Toby2")
    grouped_values = player.groupHandByValues()

    value_map = {
        1: "As", 2: "2s", 3: "3s", 4: "4s", 5: "5s", 6: "6s", 7: "7s",
        8: "8s", 9: "9s", 10: "10s", 11: "Js", 12: "Qs", 13: "Ks"
    }

    for value, key in value_map.items():
        if key in grouped_values:
            for card in grouped_values[key]:
                assert card.value == value
