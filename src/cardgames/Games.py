from cardgames import Card
from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer
import random
import time
import sys
import os
from pathlib import Path

class Games:
    TEN_SECOND_TEST = "tenSecondTest"
    FULL_TEST = "fullTest"
    REPEAT_FOREVER = "repeatForever"

    COCONUT_MALL_TRACK = "coconutMall-20min.mp3"
    FINAL_COUNTDOWN_TRACK = "finalCountdown-20min.mp3"
    GOLDFISH_TRACK = "snackThatSmilesBack-2sec.mp3"
    SMOOTH_JAZZ_TRACK = "smoothJazz-17min.mp3"

    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.assets_dir = Path(__file__).resolve().parents[2] / "assets"
        self.go_fish_sound = None
        self.valueDict = {"ace":1,"aces":1,"two":2,"twos":2,"three":3,"threes":3,"four":4,"fours":4,"five":5,"fives":5,"six":6,"sixes":6,"seven":7,
        "sevens":7,"eight":8,"eights":8,"nine":9,"nines":9,"ten":10,"tens":10,"jack":11,"jacks":11,"queen":12,"queens":12,"king":13,"kings":13}

    def choose_music_track(self):
        if random.random() < 0.8:
            return self.assets_dir / self.COCONUT_MALL_TRACK
        return self.assets_dir / self.FINAL_COUNTDOWN_TRACK

    def choose_music_playback_mode(self, input_func=input):
        prompt = (
            "Choose music mode: "
            "1) 10-second test "
            "2) full song once "
            "3) repeat forever [default]: "
        )
        choice = input_func(prompt).strip()
        while choice not in ("", "1", "2", "3"):
            choice = input_func("Invalid choice. Enter 1, 2, 3, or press Enter: ").strip()

        if choice == "1":
            return self.TEN_SECOND_TEST
        if choice == "2":
            return self.FULL_TEST
        return self.REPEAT_FOREVER

    def _ensure_audio_ready(self):
        import pygame

        if pygame.mixer.get_init() is None:
            pygame.mixer.init()

        return pygame

    def play_background_music(self, playback_mode=None, selected_track=None):
        pygame = self._ensure_audio_ready()

        if selected_track is None:
            selected_track = self.choose_music_track()
        pygame.mixer.music.load(str(selected_track))

        if playback_mode is None:
            playback_mode = self.REPEAT_FOREVER

        loops = -1 if playback_mode == self.REPEAT_FOREVER else 0
        pygame.mixer.music.play(loops)

        if playback_mode == self.TEN_SECOND_TEST:
            pygame.time.wait(10000)
            pygame.mixer.music.stop()

        return selected_track

    def play_go_fish_sound(self):
        try:
            pygame = self._ensure_audio_ready()
            if self.go_fish_sound is None:
                self.go_fish_sound = pygame.mixer.Sound(str(self.assets_dir / self.GOLDFISH_TRACK))
            self.go_fish_sound.play()
            return True
        except Exception:
            return False
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def slow_Print(self, text, delay=0.03):
        for char in text:
            print(char, end="")
            sys.stdout.flush()
            time.sleep(delay)
        print()

    def show_Title(self):
        print(r"""
    ========================================
    ▄            ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄         ▄  ▄ 
    ▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌
    ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀      ▐░█▀▀▀▀▀▀▀▀▀  ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌
    ▐░▌          ▐░▌               ▐░▌     ▐░▌               ▐░▌               ▐░▌     ▐░▌          ▐░▌       ▐░▌▐░▌
    ▐░▌          ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄      ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░▌
    ▐░▌          ▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌
    ▐░▌          ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌     ▐░█▀▀▀▀▀▀▀▀▀      ▐░▌      ▀▀▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌
    ▐░▌          ▐░▌               ▐░▌               ▐░▌     ▐░▌               ▐░▌               ▐░▌▐░▌       ▐░▌ ▀ 
    ▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄      ▐░▌      ▄▄▄▄▄▄▄▄▄█░▌     ▐░▌           ▄▄▄▄█░█▄▄▄▄  ▄▄▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌ ▄ 
    ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌     ▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌
    ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀       ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀ 
                                                                                                                    
    ========================================
        A Card Game of Chance, Choice, & Everything Inbetween
    ========================================
    """)

    def opening_Sequence(self):
        self.show_Title()

        lines = [
            "The cards are shuffled...",
            "Your opponents are ready...",
            "Time to test your luck..."
        ]

        for line in lines:
            self.slow_Print(line, 0.04)
            time.sleep(0.3)

        self.slow_Print("\nWelcome to Let's Fish!\n", 0.05)

    def show_Rules(self):
        print("\n========== HOW TO PLAY ==========")
        print("- Each player takes a turn, asking a player for a card rank (e.g., 'Aces') or drawing a card from the deck.")
        print("- If the chosen player has the requested card, they must give ALL of them.")
        print("- If not... fishing time! Draw a single card from the deck.")
        print("- The player who has the most matching sets at the end of the game wins!")
        print("(The game draws to a close as the deck empties and every card set finds their pairs).")
        print("================================\n")

    def main_Menu(self):
        while True:
            print("\n1. Start Game")
            print("2. How to Play")
            print("3. Quit")

            choice = input("\nChoose an option: ")

            if choice == "1":
                return "Starting game..."
            elif choice == "2":
                self.show_Rules()
            elif choice == "3":
                print("Bye bye!")
                exit()
            else:
                print("Please enter '1', '2', or '3'.\n")

    def run_Game(self):
        self.clear()
        self.opening_Sequence()
        choice = self.main_Menu()
        
        if choice == "Starting game...":
            print("\nStarting game...\n")

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
        self.deck.shuffle() #object.method() - games gets the shuffle ability from deck.py
        playerlist = players[:]
        random.shuffle(playerlist)
        turn_list = playerlist

        if len(players) < 4:
            cardsdealt = 7
        else:
            cardsdealt = 5
        self.dealer.dealCards(cardsdealt, turn_list)
        list.reverse(turn_list) #last dealt goes first

        self.turn_list = turn_list
        return turn_list

    def goFishing(self, player):

        print("\n"+"Go Fishing!") #Maybe replace with Prettier Font?
        self.play_go_fish_sound()
        card = self.deck.getCard()
        print(str(card))
        player.addCard(card)

        return(card)

    #this function will be called once the while loop for the main game logic is broken out of when checkFor13Books returns true
    def endGameState(self, players):
        nameScorePairs = {p.name: p.numBooks for p in players}
        mostBooks = max(nameScorePairs.values())
        mostBooksHolders = [name for name, score in nameScorePairs.items() if score == mostBooks]
        #in case of tie:
        if len(mostBooksHolders) > 1:
            print(f"It's a tie between {' and '.join(mostBooksHolders)} with {mostBooks} books each!")
        #single winner:
        else:
            winner = mostBooksHolders[0]
            print(f"{winner} wins with {mostBooks} books!")
        #scoreboard/lists all player's scores
        print("\nFinal scores:")
        for player in players:
            if player.numBooks == 0:
                print(f"{player.name} has 0 books.")
            elif player.numBooks == 1:
                print(f"{player.name}: {player.numBooks} book.\nThey have the following book: {player.books}")
                player.showBooks()
            else:
                print(f"{player.name}: {player.numBooks} books.\nThey have the following books: {player.books}")
                player.showBooks()
        print()

    def card_thievery(self, turn_list, host_player):
        player_number = []
        player_dict = {}
        for playerNum, player in enumerate(turn_list):
            if player != host_player and len(player.hand) != 0:
                player_number.append(str(playerNum))
                player_dict[(str(player.name)).lower()] = playerNum

        self.showOpponentsHands(turn_list)

        if len(player_number) == 1:
            target_choice = player_number[0]
        else:
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

        while thief_choice not in self.valueDict:
            thief_choice = (str(input("Choose card type you wish to steal: "))).lower()
            if thief_choice not in self.valueDict:
                print("Invalid Choice! Choose Card Type, eg: aces, twos, ones, etc.\n")


        stolen_cards = 0
        card_counter = 0
        target_list = target_player.hand[:]
        for card in target_list:
            if card.value == self.valueDict[thief_choice]:
                host_player.addCard(card)
                target_player.removeCard(card)
                stolen_cards += 1
        
        if stolen_cards == 0:
            self.goFishing(host_player)
            return False
        else:
            return True
        

    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')

        self.deck.shuffle() #object.method() - games gets the shuffle ability from deck.py
        try:
            self.play_background_music(
                playback_mode=self.REPEAT_FOREVER,
                selected_track=self.assets_dir / self.SMOOTH_JAZZ_TRACK
            )
        except Exception:
            print("Audio unavailable; continuing without background music.")
        
        # Access each player by "for player in players" loop OR by using indexing (player[0].name)
        players = self.create_players()
        turn_list = self.start_game(players)
        print(f"\nTurn order: {', '.join(player.name for player in turn_list)}")
        
        game_running = True #game runs until broken out of by game_running = false when all 13 books are formed
        while game_running:
            for player in turn_list:

                # Else
                input(f"\n{player.name}'s turn, when ready hit the ENTER key... ")
                player.isTurn = True
                player.takeTurn(turn_list, self)
                player.isTurn = False

                #Checks to see if game is over; there is also a check in the takeTurn function that breaks out of the turn loop when this has been met so that the game ends propperly.
                if self.dealer.checkFor13Books(players) == True:
                    game_running = False
        
        #Once main game is over, prints winner(s) & scoreboard + who made what books
        self.endGameState(players)

        input('Press [Enter] to exit.')
        

if __name__ == "__main__":
    game = Games()
    game.main()
