from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer
import random
from pathlib import Path

class Games:
<<<<<<< Updated upstream
    COCONUT_MALL_TRACK = "CoconutMall20min.mp3"
    FINAL_COUNTDOWN_TRACK = "TheFinalCountdown20min.mp3"
=======
    COCONUT_MALL_TRACK = "coconutmall20min.mp3"
    FINAL_COUNTDOWN_TRACK = "finalcountdown20min.mp3"
>>>>>>> Stashed changes
    TEN_SECOND_TEST = "ten_second_test"
    FULL_TEST = "full_test"
    REPEAT_FOREVER = "repeat_forever"

    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(Deck())
        self.assets_dir = Path(__file__).resolve().parent.parent / "assets"

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

            
    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')
        playback_mode = self.choose_music_playback_mode()
        selected_track = self.play_background_music(playback_mode)
        if selected_track is not None:
            print(f"Now playing: {selected_track.name}")
<<<<<<< Updated upstream
=======

        self.deck = Deck() #deck is created here; deck knows how, games decides when
        self.deck.shuffle() #object.method() - games gets the shuffle ability from deck.py
>>>>>>> Stashed changes
        
        # Access each player by "for player in players" loop OR by using indexing (player[0].name)
        players = self.create_players()
        turn_list = self.start_game(players) #player[0] in list goes first.

        input('Press [Enter] to exit.')
<<<<<<< Updated upstream
=======

    def choose_music_track(self):
        random_value = random.random()
        if random_value < 0.95:
            return self.assets_dir / self.COCONUT_MALL_TRACK
        return self.assets_dir / self.FINAL_COUNTDOWN_TRACK

    def choose_music_playback_mode(self, input_func=input):
        print("Music playback mode:")
        print("1. 10-second test")
        print("2. Full track once")
        print("3. Repeat forever")
        while True:
            choice = input_func("Choose playback mode (1-3, default 3): ").strip()
            if choice == "1":
                return self.TEN_SECOND_TEST
            if choice == "2":
                return self.FULL_TEST
            if choice in ("", "3"):
                return self.REPEAT_FOREVER
            print("Please choose 1, 2, or 3.")

    def play_background_music(self, playback_mode=REPEAT_FOREVER):
        try:
            import pygame
        except ImportError:
            return None

        selected_track = self.choose_music_track()
        if not selected_track.exists():
            return None

        if pygame.mixer.get_init() is None:
            pygame.mixer.init()
        pygame.mixer.music.load(str(selected_track))

        if playback_mode == self.TEN_SECOND_TEST:
            pygame.mixer.music.play(0)
            pygame.time.wait(10000)
            pygame.mixer.music.stop()
        elif playback_mode == self.FULL_TEST:
            pygame.mixer.music.play(0)
        else:
            pygame.mixer.music.play(-1)
        return selected_track


>>>>>>> Stashed changes
        
        
        print('First 5 cards in standard 52-card deck:')
        self.deck = Deck() #deck is created here; deck knows how, games decides when
        self.deck.shuffle() #object.method() - games gets the shuffle ability from deck.py

        for card in self.deck.cards[:5]:
            print(card)
        print('Press [Enter] to exit.')

    def choose_music_track(self):
        random_value = random.random()
        if random_value < 0.95:
            return self.assets_dir / self.COCONUT_MALL_TRACK
        return self.assets_dir / self.FINAL_COUNTDOWN_TRACK

    def choose_music_playback_mode(self, input_func=input):
        print("Music playback mode:")
        print("1. 10-second test")
        print("2. Full track once")
        print("3. Repeat forever")
        while True:
            choice = input_func("Choose playback mode (1-3, default 3): ").strip()
            if choice == "1":
                return self.TEN_SECOND_TEST
            if choice == "2":
                return self.FULL_TEST
            if choice in ("", "3"):
                return self.REPEAT_FOREVER
            print("Please choose 1, 2, or 3.")

    def play_background_music(self, playback_mode=REPEAT_FOREVER):
        try:
            import pygame
        except ImportError:
            return None

        selected_track = self.choose_music_track()
        if not selected_track.exists():
            return None

        if pygame.mixer.get_init() is None:
            pygame.mixer.init()
        pygame.mixer.music.load(str(selected_track))

        if playback_mode == self.TEN_SECOND_TEST:
            pygame.mixer.music.play(0)
            pygame.time.wait(10000)
            pygame.mixer.music.stop()
        elif playback_mode == self.FULL_TEST:
            pygame.mixer.music.play(0)
        else:
            pygame.mixer.music.play(-1)
        return selected_track

if __name__ == "__main__":
    game = Games()
    game.main()
