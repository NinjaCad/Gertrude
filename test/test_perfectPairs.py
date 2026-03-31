from testing_base import * 

def test_perfectPairs():
    game = Games()

    test1 = Player("test1")
    test1.hand.append(Card)
    assert test1.perfectPairs() == "Colored Pair"

    test2 = Player("test2")
    test2.hand.append(Card)
    assert test2.perfectPairs() == "Mixed Pair"

    test3 = Player("test3")
    test3.hand.append(Card)
    assert test3.perfectPairs() == False

if __name__ == "__main__":
    test_perfectPairs()