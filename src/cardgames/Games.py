from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer


class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('Welcome to the *insert name here*!')
        self.playerList = self.startGame(tr = True)
        #starts the game, output should be printed        
        self.gertDealer = Dealer(self.deck)
        for i in range(len(self.playerList)):
            self.gertDealer.dealCards(2, self.playerList)

            #may need to change the int 2 in the future,
            #not currently sure if we are going to do 1 card
            #and then another card and show the second
            #or a different method
            pass

        #call to create 
        for card in self.deck.cards[:5]:
            print(card)
        input('Press [Enter] to exit.')
    
    def startGame(self, tr):
        while tr:
            try:
                self.amtPlayers = int(input("How many people are playing? "))
                #include a minimum and maximum amount of players: https://www.w3schools.com/python/ref_keyword_raise.asp
                tr = False
            except ValueError:
                print("That doesn't make any sense, try again.")
        print('This round of blackjack will be played with {:d} players, against the dealer, GERTRUDE'.format(self.amtPlayers))
        self.pl_list = []
        for i in range(self.amtPlayers):
            self.pl_list.append(Player(input("Player {:d}'s name is: ".format(i))))
        self.pl_list.append("GERTRUDE")


        return self.pl_list

if __name__ == "__main__":
    game = Games()
    game.main()