from testing_base import *


def test_sort_grouped_cards():
    player = Player("Tim")

    cards = [
        Card("Spades", 12, 0, 0),   # Q
        Card("Hearts", 2, 0, 0),    # 2
        Card("Clubs", 13, 0, 0),    # K
        Card("Diamonds", 3, 0, 0),  # 3
        Card("Clubs", 2, 0, 0),     # 2
    ]
    player.setHand(cards)



    grouped = player.groupHandByValue()
    grouped_values_only = {key: [card.value for card in value] for key, value in grouped.items()}
    print("Grouped cards:", grouped_values_only)

    assert list(grouped.keys()) == ["2s", "3s", "Qs", "Ks"]
    assert len(grouped["2s"]) == 2
    assert len(grouped["3s"]) == 1
    assert len(grouped["Qs"]) == 1
    assert len(grouped["Ks"]) == 1

def test_sort_sorted_cards():
    player = Player("Tim")
    cards = [
        Card("Spades", 12, 0, 0),   # Q
        Card("Hearts", 2, 0, 0),    # 2
        Card("Clubs", 13, 0, 0),    # K
        Card("Diamonds", 3, 0, 0),  # 3
        Card("Clubs", 2, 0, 0),     # 2
    ]
    player.setHand(cards)
    
    sorted_cards = player.sortHandIntoValues()

    assert [card.value for card in sorted_cards] == [2, 2, 3, 12, 13]
