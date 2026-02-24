from operator import truediv

from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer


class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('Welcome to the Simple BlackJack!')
        self.playerList = self.startGame(tr = True)

        #note to self: you may need to figure out how knownCards works
        #you also may need to make it so that multiple rounds can be played 

        #starts the game, output should be printed        
        self.gertDealer = Dealer(self.deck)
        #first deal begins here
        self.gertDealer.dealCards(1, self.playerList)
        for i in range(len(self.playerList)):
            print("{:s}'s hand: ".format(self.playerList[i].name), end='')
            self.playerList[i].showHand()
        #second deal begins here
        self.gertDealer.dealCards(1, self.playerList)
        for i in range(len(self.playerList)):
            print("{:s}'s hand: ".format(self.playerList[i].name), end='')
            if self.playerList[i].name == "GERTRUDE":
                #FIGURE OUT HOW TO PRINT JUST THE BACK OF A CARD
                #AND just a single card from a hand of a player (should
                #GERTRUDE even be a player object?)
                #or make functionality in future sprint
                break
            self.playerList[i].showHand()
        #call round() here 
        self.round(self.playerList)

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
        #self.pl_list.append(Gertrude("GERTRUDE"))
        #functionality of Gertrude() will be a child class of player

        return self.pl_list

    def round(self, pList):
        # Repeat length of players minus gertrude
        for i in range(len(pList) - 1):
            # Display current hand
            print("{:s}'s hand: ".format(pList[i].name), end='')
            pList[i].showHand()
            turn = True
            while(turn): # (turn && bust() == False)      end turn if bust
                move = input('Choose either to "hit" or "stand"')
                if (move == "hit"):
                    print("hit")
                    # hit()
                elif (move == "stand"):
                    print("stand")
                    # stand()
                    turn = False
                else:
                    print("That is not a valid repsonse")
            # gertrude()


if __name__ == "__main__":
    game = Games()
    game.main()