from testing_base import *

def test_clearHand_removes_all_Cards():
    player = Player("zachary")
    
    player.hand = ["card1", "card2"]
    player.knownCards = [True, False]
    
    player.clearHand()
    assert player.hand == []
    assert player.knownCards == []
