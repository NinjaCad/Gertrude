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
    
    game = Games()
    player = Player("test")
    deck = game.deck
    dealer = game.dealer
    
    # add two cards of equal value
    for card in deck.cards:
        if card.value == 7 and card.suit == "S":
            player.addCard(card, True)
    for card in deck.cards:
        if card.value == 7 and card.suit == "D":
            player.addCard(card, True)
       
    gertrude = Player("gertrude")
    for i in range(3):
        gertrude.addCard(deck.getCard(), True)
    
    game.playerList = [ gertrude, player ]
    # guarantee split() call has appropriate results recorded     
    player.bets["standard"] = 5

    # start a game round with proper conditions to split
    game.round()
    gertrude.showHand()
    game.calculateWinner(game.playerList)
    
    # make sure print statement makes sense with player/dealer hand totals
    print(f"Final money: {player.money}")

    return


def main():
    
    test_can_split()
    
    test_split()
    
    
if __name__ == "__main__":
    main()