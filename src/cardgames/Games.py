from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer


class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('Welcome to the Simple BlackJack!')
        self.playerList = self.startGame(tr = True)
        #starts the game, output should be printed        
        self.gertDealer = Dealer(self.deck)
        self.gertDealer.dealCards(1, self.playerList)
        for i in range(len(self.playerList)):
            self.playerList[i].showHand()
        self.gertDealer.dealCards(1, self.playerList)
        for i in range(len(self.playerList)):
            if self.playerList[i].name == "GERTRUDE":
                break
            self.playerList[i].showHand()
            


        #call to create 
        for card in self.deck.cards[:5]:
            print(card)
        input('Press [Enter] to exit.')
    
    def startGame(self, tr):
        while tr:
            try:
                self.amtPlayers = int(input("How many people are playing? (7 players max.) "))
                #include a minimum and maximum amount of players: https://www.w3schools.com/python/ref_keyword_raise.asp
                if self.amtPlayers > 7:
                    raise Exception("That's too many players! Try again.")
                if self.amtPlayers < 1:
                    raise Exception("There needs to be at least one player! Try again.")
                tr = False
            except ValueError:
                print("That doesn't make any sense, try again.")
        print('This round of blackjack will be played with {:d} players, against the dealer, GERTRUDE'.format(self.amtPlayers))
        self.pl_list = []
        for i in range(self.amtPlayers):
            self.pl_list.append(Player(input("Player {:d}'s name is: ".format(i))))
        self.pl_list.append(Player("GERTRUDE"))


        return self.pl_list

if __name__ == "__main__":
    game = Games()
    game.main()