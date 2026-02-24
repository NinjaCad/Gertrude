from testing_base import *

pl = Player("John")

def test_check_cards():
    assert pl.check_cards([0, 0]) == 12
    
def test_check_cards2():   
    assert pl.check_cards([0,5]) == 17

def test_check_cards3():
    assert pl.check_cards([9,9,0]) == 21

def test_check_cards4(): 
    assert pl.check_cards([0,0,0,0,14]) == 16

