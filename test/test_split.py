from testing_base import *


def test_can_split():
    
    player = Player("test")
    deck = Deck()
    
    # test case 1: less than 2 cards
    card1 = None
    for card in deck.cards:
        if card.value == 7 and card.suit == "S":
            player.addCard(card, True)
            card1 = card
            break
        
    assert player.can_split() == False
    
    
    # test case 2: 2 unequal cards 
    card2 = None
    for card in deck.cards:
        if card.value != 7:
            player.addCard(card, True)
            card2 = card
            break
        
    assert player.can_split() == False
    
    
    # test case 3: 2 equal cards
    for card in deck.cards:
        if card.value == 7 and card.suit == "D":
            player.setHand([card1, card], True)
            break

    assert player.can_split() == True
    
    
    # test case 4: 2 equal cards but not enough money
    player.bets["standard"] = 10
    player.money = -85
    assert player.can_split() == False
    
    
    # test case 5: 2 equal cards but more than 2 cards
    player.addCard(card2, True)
    assert player.can_split() == False
    
    return


def test_split():
    
    player = Player("test")
    deck = Deck()
    dealer = Dealer(deck)
    
    # add two cards of equal value
    for card in deck.cards:
        if card.value == 7 and card.suit == "S":
            player.addCard(card, True)
    for card in deck.cards:
        if card.value == 7 and card.suit == "D":
            player.addCard(card, True)
       
    # guarantee split() call has appropriate results recorded     
    player.bets["standard"] = 5
    player.split(dealer)
    assert player.split_hands_score
    
    # guarantee resolve_bet_split() resolves unique split() bets correctly and resets properly
    print(f"Hand scores: {player.split_hands_score}")
    print(f"Dealer score: 17")
    print(f"Player originally as $100. Bet is $5, so players final money should be from 90-110 based on whether or not each hand wins.")
    player.resolve_bet_split(17) # test w/ dealerScore of 17
    print(f"Final money {player.money}")
    assert player.bets["standard"] == 0
    assert player.split_hands_score == None

    return


def main():
    
    test_can_split()
    
    
if __name__ == "__main__":
    main()