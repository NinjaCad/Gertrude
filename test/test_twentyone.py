from testing_base import * 

# test if player only has one card
def test_playerCards():
    test = Player("test")
    test.bets["21+3"] = 1
    dealerCard = Card("S", 0, None, None)
    test.hand.append(Card("S", 0, None, None))
    assert test.twentyone(dealerCard) == False
    assert test.bets["21+3"] == 1

# Test if dealer has no card
def test_dealerCard():
    test = Player("test")
    test.bets["21+3"] = 1
    test.hand.append(Card("S", 0, None, None))
    test.hand.append(Card("H", 0, None, None))
    assert test.twentyone() == False
    assert test.bets["21+3"] == 1

# Test no winning hands
def test_noWin():
    test = Player("test")
    test.bets["21+3"] = 1
    test.hand.append(Card("S", 1, None, None))
    test.hand.append(Card("H", 3, None, None))
    dealerCard = Card("D", 5, None, None)
    assert test.twentyone(dealerCard) == False
    assert test.bets["21+3"] == 1

# Test flush
def test_flush():
    test = Player("test")
    test.bets["21+3"] = 1
    test.hand.append(Card("S", 1, None, None))
    test.hand.append(Card("S", 3, None, None))
    dealerCard = Card("S", 5, None, None)
    assert test.twentyone(dealerCard) == True
    assert test.bets["21+3"] == 5

# Test low straight
def test_lowStraight():
    test = Player("test")
    test.bets["21+3"] = 1
    test.hand.append(Card("S", 1, None, None))
    test.hand.append(Card("D", 2, None, None))
    dealerCard = Card("H", 3, None, None)
    assert test.twentyone(dealerCard) == True
    assert test.bets["21+3"] == 10

# Test high straight
def test_highStraight():
    test = Player("test")
    test.bets["21+3"] = 1
    test.hand.append(Card("S", 12, None, None))
    test.hand.append(Card("D", 13, None, None))
    dealerCard = Card("H", 1, None, None)
    assert test.twentyone(dealerCard) == True
    assert test.bets["21+3"] == 10

# Test three of a kind
def test_threeKind():
    test = Player("test")
    test.bets["21+3"] = 1
    test.hand.append(Card("S", 6, None, None))
    test.hand.append(Card("D", 6, None, None))
    dealerCard = Card("H", 6, None, None)
    assert test.twentyone(dealerCard) == True
    assert test.bets["21+3"] == 30

# Test low straight flush
def test_lowStraightFlush():
    test = Player("test")
    test.bets["21+3"] = 1
    test.hand.append(Card("S", 1, None, None))
    test.hand.append(Card("S", 2, None, None))
    dealerCard = Card("S", 3, None, None)
    assert test.twentyone(dealerCard) == True
    assert test.bets["21+3"] == 40

# Test high straight flush
def test_highStraightFlush():
    test = Player("test")
    test.bets["21+3"] = 1
    test.hand.append(Card("S", 12, None, None))
    test.hand.append(Card("S", 13, None, None))
    dealerCard = Card("S", 1, None, None)
    assert test.twentyone(dealerCard) == True
    assert test.bets["21+3"] == 40