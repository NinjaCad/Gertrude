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

def check.cards(pl, hand):
      
    card_values = {}

    for i in range(52):
        rank_index = i % 13  # 0=Ace, 1=Two ... 10=Jack, 11=Queen, 12=King

        if rank_index == 0:
            val = 11        # Ace
        elif rank_index >= 10:
            val = 10        # Jack, Queen, King
        else:
            val = rank_index + 1 # 2-10 (Index 1 is card '2', Index 9 is card '10')
        
    card_values[i] = val

    card_values[0]

    # total = sum(hand)
    # ace_count = hand.count(11)

    # # Downgrade Aces from 11 to 1 if busted
    # while total > 21 and ace_count > 0:
    #     total -= 10   # 11 → 1
    #     ace_count -= 1

    # return total

if __name__ == "__main__":
    game = Games()
    game.main()
 
 

