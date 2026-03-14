from cardgames import Card
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

    def card_thievery(self, turn_list, host_player):
        stepper = 1
        for players in turn_list:
            print("player "+str(stepper)+" "+str(players)+" cards: "+str(len(players.hand))) #Prints players and amount of cards
            stepper += 1

        target_choice = int(0)
        while target_choice > len(turn_list) or target_choice <= 0:
            target_choice = int(input("/n"+"Choose player number to steal from: "+"/n"))
            if target_choice > len(turn_list) or target_choice <= 0:
                print("Invalid Input! Enter player number.")
        target_player = turn_list(target_choice - 1)

        #print("Put Card Names Here /n") #Place types of cards here, need card IDs
        print("Current Hand: ")
        print(host_player.hand)
        print("")

        thief_choice = 0
        while thief_choice > len(target_player.hand) or thief_choice <= 0: #FIX #Needs to have card id#s
            print("Targets Hand Length: "+str(len(target_player.hand)))
            thief_choice = int(input("Choose card you wish to steal: "))
            if thief_choice > len(target_player.hand) or thief_choice <= 0:
                print("Invalid Choice! Choose number between 0 and "+str(len(target_player.hand)))
        stolen_card = target_player.hand(thief_choice) #Temporary Card Choice until Card IDs
        
        return stolen_card

        

            
    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')

        self.deck = Deck() #deck is created here; deck knows how, games decides when
        self.deck.shuffle() #object.method() - games gets the shuffle ability from deck.py
        
        # Access each player by "for player in players" loop OR by using indexing (player[0].name)
        players = self.create_players()
        turn_list = self.start_game(players)
        
        game_running = True #game essentially runs forever. logic is needed to state when the game ends!!!!
        while game_running:
            for player in turn_list:
                print(player.name)

                card_steal = True
                while card_steal == True:
                    thief_answer = (str(input("Would you like to steal a card?"))).lower()
                    if thief_answer == "y" or "yes":
                        self.card_thievery(turn_list, player)
                    elif thief_answer == "n" or "no":
                        card_steal = False
                    else:
                        print("Invalid Input, Type 'y' for Yes or 'n' for No.")

        #for each player in the turn list:
            #that player takes a turn

        

if __name__ == "__main__":
    game = Games()
    game.main()