from cardgames.Deck import Deck

class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')
        
        print('First 5 cards in standard 52-card deck:')
        temp = 0
        for card in self.deck.cards[:52]:
            print(temp, card)
            temp += 1
        input('Press [Enter] to exit.')

# def aceLogic(hand):
    
#     ace = 0, 

#     total = sum(hand)
#     ace_count = hand.count(11)

#     # Downgrade Aces from 11 to 1 if busted
#     while total > 21 and ace_count > 0:
#         total -= 10   # 11 → 1
#         ace_count -= 1

#     return total

if __name__ == "__main__":
    game = Games()
    game.main()
 
 

