from testing_base import *


def test_can_double():
    
    player = Player("test")
    deck = Deck()
    deck.shuffle()
    
    # test case 1: first turn, not enough money (FALSE)
    # using insurance also tests new helper method bet_totals() in Player.py
    player.bets["standard"] = 10
    player.bets["insurance"] = 15
    player.money = 30
    for i in range(2):
        card = deck.getCard()
        player.addCard(card, True)   
    assert player.can_double() == False
    
    # test case 2: first turn, enough money (TRUE)
    player.bets["insurance"] = 10
    assert player.can_double() == True
    
    # test case 3: not first turn, enough money (FALSE)
    card = deck.getCard()
    player.addCard(card, True)
    assert player.can_double() == False
    
    # test case 4: not first turn, not enough money (FALSE)
    player.bets["standard"] = 20
    assert player.can_double() == False
    
    return


def test_double_down():
    
    player = Player("test")
    deck = Deck()
    dealer = Dealer(deck)

    player.money = 100
    player.bets["standard"] = 10

    for i in range(2):
        card = deck.getCard()
        player.addCard(card, True)
        
    player.double_down(dealer)

    assert player.bets["standard"] == 20
    assert len(player.hand) == 3
    assert player.active == False

    return