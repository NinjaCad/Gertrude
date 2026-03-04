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





if __name__ == "__main__":
    game = Games()
    game.main()
 
 

