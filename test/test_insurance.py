from testing_base import *


def test_insurance():
    players = [Player("Gertrude"), Player("Bob")]
    players[0].hand.append(Card("S", 1, None, None))
    players[0].hand.append(Card("H", 10, None, None))
    assert players[1].insurance(players) == True

    
def test_no_insurance():
    players = [Player("Gertrude"), Player("Bob")]
    players[0].hand.append(Card("S", 2, None, None))
    players[0].hand.append(Card("H", 10, None, None))
    assert players[1].insurance(players) == False
    
                       
