from testing_base import *

pl = Player("John")

def test_check_cards():
    # Two Aces -> 11 + 11 = 22
    # Adjust one Ace from 11 to 1 -> total = 12
    assert pl.check_cards([0, 0]) == 12
    
def test_check_cards2():
    # 5 % 13 == 5 -> 6
    # 11 + 6 = 17 (no adjustment needed)  
    assert pl.check_cards([0,5]) == 17

def test_check_cards3():
    # 9 % 13 == 9 -> 10
    # 0 % 13 == 0 -> Ace (11)
    # 10 + 10 + 11 = 31
    # Adjust Ace from 11 to 1 -> total = 21
    assert pl.check_cards([9,9,0]) == 21

def test_check_cards4():
    # 0,0,0,0 -> four Aces -> 11*4 = 44
    # 14 % 13 == 1 -> 2
    # 44 + 2 = 46
    # Adjust Aces from 11 to 1 as needed:
    # 46 -> 36 -> 26 -> 16 (three adjustments)
    # Final total = 16 
    assert pl.check_cards([0,0,0,0,14]) == 16

def test_check_cards5():
    # 52, 65, 78 all % 13 == 0 -> three Aces -> 11*3 = 33 -> adjust -> 13
    assert pl.check_cards([52, 65, 78]) == 13

def test_check_cards6():
    # 12 % 13 == 12 -> King -> 10
    # 25 % 13 == 12 -> King -> 10
    # 38 % 13 == 12 -> King -> 10
    # 10 + 10 + 10 = 30 (bust)
    assert pl.check_cards([12, 25, 38]) == 30

def test_check_cards7():
    # 51 % 13 == 12 -> King -> 10
    # 39 % 13 == 0 -> Ace (11)
    # 10 + 11 = 21 (blackjack)
    assert pl.check_cards([51, 39]) == 21

