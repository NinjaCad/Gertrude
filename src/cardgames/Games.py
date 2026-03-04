from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer


class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('Welcome to the Simple BlackJack!')
        self.playerList = self.startGame()
        
        print('This games application is under development.')
        
        print('First 5 cards in standard 52-card deck:')
        temp = 0
        for card in self.deck.cards[:52]:
            print(temp, card)
            temp += 1
        input('Press [Enter] to exit.')

    
    def startGame(self):
        while True:
            try:
                self.amtPlayers = int(input("How many people are playing? (7 players max.) "))
                
                if self.amtPlayers > 7:
                    print("That's too many players! Try again.")
                    continue
                if self.amtPlayers < 1:
                    print("There needs to be at least one player! Try again.")
                    continue
                break
            except ValueError:
                print("That doesn't make any sense, try again.")
        print('This round of blackjack will be played with {:d} players, against the dealer, GERTRUDE'.format(self.amtPlayers))
        self.pl_list = []
        for i in range(self.amtPlayers):
            self.pl_list.append(Player(str(input("Player {:d}'s name is: ".format(i+1)))))
        self.pl_list.append(Player("GERTRUDE"))
        #Player("GERTRUDE") will be eventually replaced 

        return self.pl_list






if __name__ == "__main__":
    game = Games()
    game.main()
 
 

