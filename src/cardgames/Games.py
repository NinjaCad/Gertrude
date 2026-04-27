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
        self.valueDict = {"a":1,"ace":1,"aces":1,"two":2,"twos":2,"three":3,"threes":3,"four":4,"fours":4,"five":5,"fives":5,"six":6,"sixes":6,"seven":7,
        "sevens":7,"eight":8,"eights":8,"nine":9,"nines":9,"ten":10,"tens":10,"j":11,"jack":11,"jacks":11,"q":12,"queen":12,"queens":12,"k":13,"king":13,"kings":13}

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


    class UI:
        TITLE = r"""
__| |___________________________________________________________________| |__
__   ___________________________________________________________________   __
  | |                                                                   | |  
  | |██╗     ███████╗████████╗███████╗    ███████╗██╗███████╗██╗  ██╗██╗| |  
  | |██║     ██╔════╝╚══██╔══╝██╔════╝    ██╔════╝██║██╔════╝██║  ██║██║| |  
  | |██║     █████╗     ██║   ███████╗    █████╗  ██║███████╗███████║██║| |  
  | |██║     ██╔══╝     ██║   ╚════██║    ██╔══╝  ██║╚════██║██╔══██║╚═╝| |  
  | |███████╗███████╗   ██║   ███████║    ██║     ██║███████║██║  ██║██╗| |  
  | |╚══════╝╚══════╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝| |  
__| |___________________________________________________________________| |__
__   ___________________________________________________________________   __
  | |                                                                   | |  
                                                                                                                                                 
            A Card Game of Chance, Choice, & Everything Inbetween
    """
    
        go_fishing = r"""
 ██████╗  ██████╗     ███████╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ ██╗
██╔════╝ ██╔═══██╗    ██╔════╝██║██╔════╝██║  ██║██║████╗  ██║██╔════╝ ██║
██║  ███╗██║   ██║    █████╗  ██║███████╗███████║██║██╔██╗ ██║██║  ███╗██║
██║   ██║██║   ██║    ██╔══╝  ██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║╚═╝
╚██████╔╝╚██████╔╝    ██║     ██║███████║██║  ██║██║██║ ╚████║╚██████╔╝██╗
 ╚═════╝  ╚═════╝     ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝
    """
    
        RULES = r"""
\n========== HOW TO PLAY ==========")
("- Each player takes a turn, asking a player for a card rank (e.g., 'Aces') or drawing a card from the deck.")
("- If the chosen player has the requested card, they must give ALL of them.")
("- If not... fishing time! Draw a single card from the deck.")
("- The player who has the most matching sets at the end of the game wins!")
("(The game draws to a close as the deck empties and every card set finds their pairs).")
("================================\n
    """
        
    def slow_print(self, text, delay=0.03):
        for char in text:
            print(char, end="")
            sys.stdout.flush()
            time.sleep(delay)
        print()
    
    def opening_Sequence(self):
        print(self.UI.TITLE)
        lines = [
            "The cards are shuffled...",
            "Your opponents are ready...",
            "Time to test your luck..."
        ]
        for line in lines:
            self.slow_print(line, 0.04)
    
    def choose_Game_mode(self):
        modeDict = {"2":"speedy","3":"hyper","1":"regular"}
        print("\nSelect Game Mode:")
        print("1. Regular (standard dealing)")
        print("2. Speedy (10 cards each)")
        print("3. hyper mode (13 card dealt)")
        gameMode = str(input("\nChoose an option: "))
        while gameMode.lower() not in ["speedy","hyper","regular"]:
            if gameMode in modeDict:
                gameMode = modeDict[gameMode]
            else:
                print("Invalid Input! \n")
                gameMode = input(str("Choose an option: "))
        return gameMode.lower()

    def main_Menu(self):
        while True:
            print("\n1. Start Game")
            print("2. How to Play")
            print("3. Quit")
            choice = input("\nChoose an option: ")
            if choice == "1":
                return True
            elif choice == "2":
                print(self.UI.RULES)
            elif choice == "3":
                print("Bye bye!")
                exit()
            else:
                print("Please enter '1', '2', or '3'.\n")


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
    
    def start_game(self, players, mode=None):
        self.deck.shuffle() #object.method() - games gets the shuffle ability from deck.py
        playerlist = players[:]
        random.shuffle(playerlist)
        if mode == None:
            mode = self.choose_Game_mode()
        
        if mode == "speedy":
            cardsdealt = 10
        elif mode == "hyper":
            cardsdealt = 13
        else:
            cardsdealt = 7 if len(players) < 4 else 5

        print(f"{mode.capitalize()} Mode: Dealing {cardsdealt} cards each")
        self.dealer.dealCards(cardsdealt, playerlist)
        list.reverse(playerlist) #last dealt goes first

        self.turn_list = playerlist
        return playerlist
    
    def initialBookCheck(self, players):
        for player in players:
            player.bookHandling()
            if player.books != []:
                print(f"\n{player.name} started the following books:")
                player.showBooks()

    def goFishing(self, player):
        print(self.UI.go_fishing)
        card = self.deck.getCard()
        print(f"You drew: \n{card}")
        player.addCard(card)
        return card

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

    def playersWithCards(self, turn_list, host_player): #Players who still have cards

        playerNumberList = []
        player_dict = {}
        
        for playerNum, player in enumerate(turn_list):
            if len(player.hand) != 0:
                if turn_list[playerNum] != host_player:
                    playerNumberList.append(playerNum)
                    player_dict[(str(player.name)).lower()] = playerNum
        return(playerNumberList, player_dict)

    def card_thievery(self, turn_list, host_player):
        playerNumber, playerDict = self.playersWithCards(turn_list, host_player)
        self.showOpponentsHands(turn_list)

        if len(playerNumber) == 1:
            targetNumber = playerNumber[0]
        else:
            targetNumber = -1
        while targetNumber not in playerNumber:
            targetChoice = (str(input("\n"+"Choose player to steal from: "))).lower()
            if targetChoice in playerDict:
                if turn_list[playerDict[targetChoice]] == host_player:
                    print("Invalid Input! You cannot choose yourself!")
                else:
                    targetNumber = int(playerDict[targetChoice])
            elif targetChoice in ["0","1","2","3"]:
                if int(targetChoice) not in playerNumber:
                    print("Invalid Input! You cannot choose player with no cards!")
                elif turn_list[int(targetChoice)] == host_player:
                    print("Invalid Input! You cannot choose yourself!")
                else:
                    targetNumber = int(targetChoice)
            else:
                print("Invalid Input! Enter player name or number.")

        target_player = turn_list[int(targetNumber)]
        print("")
        
        valuesInHand = []
        for card in host_player.hand:
            if card.value not in valuesInHand:
                valuesInHand.append(card.value)

        thief_choice = None
        host_player.hand = host_player.sortHandIntoValues()
        while thief_choice not in valuesInHand:
            host_player.showHand()
            thief_choice = (str(input("Choose card type you wish to steal: "))).lower()
            
            if thief_choice in self.valueDict:
                thief_choice = self.valueDict[thief_choice]
            elif thief_choice in ["1","2","3","4","5","6","7","8","9","10","11","12","13"]:
                thief_choice = int(thief_choice)
            if thief_choice not in valuesInHand:
                print("You must choose a card you have in hand! ")

        stolen_cards = 0
        target_list = target_player.hand[:]
        for card in target_list:
            if card.value == thief_choice:
                host_player.addCard(card)
                target_player.removeCard(card)
                stolen_cards += 1
        
        if stolen_cards == 0: #if they went fishing:
            pickedCard = self.goFishing(host_player)
            return False, thief_choice, pickedCard
        else:
            return True, None, None
        

    def main(self):

        self.opening_Sequence()
        self.deck.shuffle()
        game_running = self.main_Menu()

        try:
            self.play_background_music(
                playback_mode=self.REPEAT_FOREVER,
                selected_track=self.assets_dir / self.SMOOTH_JAZZ_TRACK
            )
        except Exception:
            print("Audio unavailable; continuing without background music.")

        players = self.create_players()
        turn_list = self.start_game(players)
        print(f"\nTurn order: {', '.join(player.name for player in turn_list)}")
        
        while game_running:
            for player in turn_list:
                
                print("\n"*20)
                input(f"\n{player.name}'s turn, when ready hit the ENTER key... ")
                player.isTurn = True
                player.takeTurn(turn_list, self)
                
                player.isTurn = False
                if self.dealer.checkFor13Books(turn_list):
                    game_running = False
    
        self.endGameState(players)
        

if __name__ == "__main__":
    game = Games()
    game.main()
