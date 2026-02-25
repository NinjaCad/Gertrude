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
        accepted_player_count = [2,3,4]
        player_names = []
        while True:
            try:
                # Creates between 2 and 4 players
                num_of_players = int(input("Enter amount of players (2-4): "))
                if num_of_players in accepted_player_count:

                    # Inputting player name
                    for i in range(num_of_players):
                        while True:
                            player = input(f"Enter name of player {i + 1}: ")
                            if player == '':
                                print("Please enter a name.")
                            elif player in player_names:
                                print("Name must be unique!")
                            elif len(player) > 16:
                                print("Name too long! Must be under 17 characters.")
                            else:
                                players.append(Player(player))
                                player_names.append(player)
                                break
                    break
                else:
                    print("Must be a positive integer between 2 and 4!")
            except ValueError:
                print("Must be a valid number!")
        return players
    
    def start_game(self, players):
        turn_list = players[:]
        random.shuffle(turn_list)

        if len(players) < 4:
            cardsdealt = 7
        else:
            cardsdealt = 5
        for xyz in (range(cardsdealt)):
            self.dealer.dealCards(1, turn_list)
        
        list.reverse(turn_list)
        #First player in list goes first.
        return turn_list

    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')
        
        # Access each player by "for player in players" loop OR by using indexing (player[0].name)
        players = self.create_players()
        turn_list = self.start_game(players)

        input('Press [Enter] to exit.')

if __name__ == "__main__":
    game = Games()
    game.main()