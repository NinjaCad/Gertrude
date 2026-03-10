from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer
import random

class Games:

    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(Deck())

    def create_players(self):
        players = []
        acceptedPlayerCount = [2,3,4]
        playerNames = []
        while True:
            try:
                # Creates between 2 and 4 players
                numOfPlayers = int(input("Enter amount of players (2-4): "))
                if numOfPlayers in acceptedPlayerCount:

                    # Inputting player name
                    for i in range(numOfPlayers):
                        while True:
                            player = input(f"Enter name of player {i + 1}: ")
                            if player.strip() == '':
                                print("Please enter a name.")
                            elif player in playerNames:
                                print("Name must be unique!")
                            elif len(player) > 16:
                                print("Name is too long! Must be under 17 characters.")
                            else:
                                players.append(Player(player))
                                playerNames.append(player)
                                break
                    break
                else:
                    print("Must be a positive integer between 2 and 4!")
            except ValueError:
                print("Must be a valid number!")
        return players
    
    def showOpponentsHands(self, players):
        for player in players:
            if player.isTurn or player.hand == []:
                continue
            
            # Turns player.knownCards into Falses to only print the backs, then restores it afterwords
            print(f'{player.name}\'s hand:')
            knownCardsStore = player.knownCards
            player.knownCards = [False] * len(player.knownCards)

            player.showHand()
            print()

            player.knownCards = knownCardsStore
    
    def start_game(self, players):
        playerlist = players[:]
        random.shuffle(playerlist)
        turn_list = playerlist

        if len(players) < 4:
            cardsdealt = 7
        else:
            cardsdealt = 5
        self.dealer.dealCards(cardsdealt, turn_list)
        list.reverse(turn_list) #last dealt goes first

        return turn_list

            
    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')
        
        # Access each player by "for player in players" loop OR by using indexing (player[0].name)
        players = self.create_players()
        turn_list = self.start_game(players) #player[0] in list goes first.

        input('Press [Enter] to exit.')
        
        
        print('First 5 cards in standard 52-card deck:')
        self.deck = Deck() #deck is created here; deck knows how, games decides when
        self.deck.shuffle() #object.method() - games gets the shuffle ability from deck.py

        for card in self.deck.cards[:5]:
            print(card)
        print('Press [Enter] to exit.')

if __name__ == "__main__":
    game = Games()
    game.main()