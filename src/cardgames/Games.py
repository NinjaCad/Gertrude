from cardgames import Card
from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer
import random

class Games:

    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)

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
        print()
        for playerNum, player in enumerate(players):
            if player.isTurn or player.hand == []: # Skips the player whos turn it is, as well as players with empty hands
                continue
            
            print(f'({playerNum}) {player.name}\'s hand:')
            knownCardsStore = player.knownCards
            player.knownCards = [False] * len(player.knownCards) # Changes cards in opponents' hands to not be visible

            player.showHand()
            print()

            player.knownCards = knownCardsStore # Reverses cards to be visible
    
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
        player_number = []
        player_dict = {}
        for playerNum, player in enumerate(turn_list):
            if player != host_player and len(player.hand) != 0:
                player_number.append(str(playerNum))
                player_dict[(str(player.name)).lower()] = playerNum

        self.showOpponentsHands(turn_list)

        target_choice = ""
        while target_choice not in player_number:
            target_choice = (str(input("\n"+"Choose player to steal from: "))).lower()
            if target_choice in player_dict:
                target_choice = str(player_dict[target_choice])
            elif target_choice not in player_number and target_choice not in player_dict:
                print("Invalid Input! Enter player name or number.")
                target_choice = ""
        target_player = turn_list[int(target_choice)]
        print("")

        #print("Put Card Names Here /n") #Place types of cards here
        #print(host_player.hand) #Put Function for showing cards in hand here

        thief_choice = 0
        value_dict = {"ace":1,"aces":1,"two":2,"twos":2,"three":3,"threes":3,"four":4,"fours":4,"five":5,"fives":5,"six":6,"sixes":6,"seven":7,
        "sevens":7,"eight":8,"eights":8,"nine":9,"nines":9,"ten":10,"tens":10,"jack":11,"jacks":11,"queen":12,"queens":12,"king":13,"kings":13}

        while thief_choice not in value_dict:
            thief_choice = (str(input("Choose card type you wish to steal: "))).lower()
            if thief_choice not in value_dict:
                print("Invalid Choice! Choose Card Type, eg: aces.\n")

        stolen_cards = 0
        card_counter = 0
        target_list = target_player.hand[:]
        for card in target_list:
            if card.value == value_dict[thief_choice]:
                host_player.addCard(card)
                target_player.removeCard(card)
                stolen_cards += 1
            card_counter += 1
        
        if stolen_cards == 0:
            print("Go Fish!") #Place Go Fish Here
            return False
        else:
            return True
        

    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')

        self.deck.shuffle() #object.method() - games gets the shuffle ability from deck.py
        
        # Access each player by "for player in players" loop OR by using indexing (player[0].name)
        players = self.create_players()
        turn_list = self.start_game(players)
        print(f"\nTurn order: {", ".join(player.name for player in turn_list)}")
        
        game_running = True #game essentially runs forever. logic is needed to state when the game ends!!!!
        while game_running:
            for player in turn_list:

                # Else
                input(f"\n{player.name}'s turn, when ready hit the ENTER key... ")
                player.isTurn = True
                player.takeTurn(turn_list, self)

                player.isTurn = False
    
        input('Press [Enter] to exit.')
        

if __name__ == "__main__":
    game = Games()
    game.main()