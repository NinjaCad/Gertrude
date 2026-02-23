from cardgames.Deck import Deck

class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('Welcome to the *insert name here*!')
        amt = self.startGame(tr = True)        
        print('First 5 cards in standard 52-card deck:')
        for card in self.deck.cards[:5]:
            print(card)
        input('Press [Enter] to exit.')
    
    def startGame(self, tr):
        while tr:
            try:
                amtPlayers = int(input("How many people are playing?"))
                tr = False
            except ValueError:
                print("That doesn't make any sense, try again.")
        print("out of startGame, returning to main")
        return amtPlayers

if __name__ == "__main__":
    game = Games()
    game.main()