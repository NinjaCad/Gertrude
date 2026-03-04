from cardgames.Deck import Deck

class Games:
            
    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')
        
        print('First 5 cards in standard 52-card deck:')
        self.deck = Deck() #deck is created here; deck knows how, games decides when
        self.deck.shuffle() #object.method() - games gets the shuffle ability from deck.py

        for card in self.deck.cards[:5]:
            print(card)
        print('Press [Enter] to exit.')

if __name__ == "__main__":
    game = Games()
    game.main()