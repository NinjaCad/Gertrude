from testing_base import *


def test_betting():
    
    print("Test using 50 for first bet input and 100 for second bet input.")
    
    # confirm attributes are correctly initialized
    PlayerA = Player("Test")
    assert PlayerA.money == 100
    assert PlayerA.bet_money == 0
    
    # confirm bet() edits player.bet_money but doesn't yet affect player.money
    PlayerA.bet() # test 50 for first input
    assert PlayerA.money == 100
    assert PlayerA.bet_money == 50
    
    # initialize fake dealer to test resolve_bet()
    dealer = Player("Dealer")
    assert dealer.money == 100
    
    # make sure upon win, player gets money, dealer loses money, and bet is reset
    PlayerA.resolve_bet(True, dealer)
    assert PlayerA.money == 150
    assert dealer.money == 50
    assert PlayerA.bet_money == 0
    
    # make sure upon loss, player loses money, dealer gets money, and bet is reset
    PlayerA.bet() # test 100 for second input
    PlayerA.resolve_bet(False, dealer)
    assert PlayerA.money == 50
    assert dealer.money == 150
    assert PlayerA.bet_money == 0


def main():
    test_betting()
    
    
if __name__ == "__main__":
    main()