from testing_base import * 

# Colored Pairs
def test_perfectPairsC():
    test1 = Player("test1")
    test1.bets["pairs"] = 10
    test1.hand.append(Card("S", 0, None, None))
    test1.hand.append(Card("C", 0, None, None))
    # Test if perfect pair succeeded
    assert test1.perfectPairs() == True
    # Test if the amount of money gets multplied with the correct pair
    assert test1.bets["pairs"] == 100

# Mixed Pairs
def test_perfectPairsM():
    test2 = Player("test2")
    test2.bets["pairs"] = 10
    test2.hand.append(Card("S", 0, None, None))
    test2.hand.append(Card("H", 0, None, None))
    # Test if perfect pair succeeded
    assert test2.perfectPairs() == True
    # Test if the amount of money gets multplied with the correct pair
    assert test2.bets["pairs"] == 50

# Failed Pair
def test_perfectPairsF():
    test3 = Player("test3")
    test3.bets["pairs"] = 10
    test3.hand.append(Card("S", 0, None, None))
    test3.hand.append(Card("S", 1, None, None))
    # Test if perfect pair succeeded
    assert test3.perfectPairs() == False
    # Test if the bet doesn't get multiplied
    assert test3.bets["pairs"] == 10