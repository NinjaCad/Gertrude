from cardgames import Card
from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer
import random
from pathlib import Path


class Games:
    COCONUT_MALL_TRACK = "CoconutMall20min.mp3"
    FINAL_COUNTDOWN_TRACK = "TheFinalCountdown20min.mp3"
    TEN_SECOND_TEST = "ten_second_test"
    FULL_TEST = "full_test"
    REPEAT_FOREVER = "repeat_forever"

    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(Deck())
        self.assets_dir = Path(__file__).resolve().parent.parent / "assets"

    def create_players(self):
        players = []
        acceptedPlayerCount = [2, 3, 4]
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
                            if player.strip() == "":
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
            # Skips the player whose turn it is, and players with empty hands
            if player.isTurn or player.hand == []:
                continue

            print(f"{player.name}'s hand:")
            knownCardsStore = player.knownCards
            # Changes cards in opponents' hands to not be visible
            player.knownCards = [False] * len(player.knownCards)

            player.showHand()
            print()

            player.knownCards = knownCardsStore  # Reverses cards to be visible

    def start_game(self, players):
        playerlist = players[:]
        random.shuffle(playerlist)
        turn_list = playerlist

        if len(players) < 4:
            cardsdealt = 7
        else:
            cardsdealt = 5
        self.dealer.dealCards(cardsdealt, turn_list)
        list.reverse(turn_list)  # last dealt goes first

        return turn_list

    def card_thievery(self, turn_list, host_player):
        stepper = 1
        player_number = []
        player_dict = {}
        for players in turn_list:
            if players != host_player and len(players.hand) != 0:
                # Prints players and amount of cards
                print("player " + str(stepper) + ": " + str(players.name) + " cards: " + str(len(players.hand)))
                player_number.append(str(stepper))
                player_dict[(str(players.name)).lower()] = stepper

            stepper += 1

        target_choice = ""
        while target_choice not in player_number:
            target_choice = (str(input("\n" + "Choose player to steal from: "))).lower()
            if target_choice in player_dict:
                target_choice = str(player_dict[target_choice])
            elif target_choice not in player_number and target_choice not in player_dict:
                print("Invalid Input! Enter player name or number.")
                target_choice = ""
        target_player = turn_list[int(target_choice) - 1]
        print("")

        thief_choice = 0
        value_dict = {
            "ace": 1, "aces": 1, "two": 2, "twos": 2, "three": 3, "threes": 3, "four": 4, "fours": 4,
            "five": 5, "fives": 5, "six": 6, "sixes": 6, "seven": 7, "sevens": 7, "eight": 8, "eights": 8,
            "nine": 9, "nines": 9, "ten": 10, "tens": 10, "jack": 11, "jacks": 11, "queen": 12, "queens": 12,
            "king": 13, "kings": 13
        }

        while thief_choice not in value_dict:
            thief_choice = (str(input("Choose card type you wish to steal: "))).lower()
            if thief_choice not in value_dict:
                print("Invalid Choice! Choose Card Type, eg: aces.")

        stolen_cards = 0
        target_list = target_player.hand[:]
        for card in target_list:
            if card.value == value_dict[thief_choice]:
                host_player.addCard(card)
                target_player.removeCard(card)
                stolen_cards += 1

        if stolen_cards == 0:
            print("Go Fish!")  # Place Go Fish Here

        return target_player

    def main(self):
        print("Welcome to the Games application!")
        print("This games application is under development.")
        playback_mode = self.choose_music_playback_mode()
        selected_track = self.play_background_music(playback_mode)
        if selected_track is not None:
            print(f"Now playing: {selected_track.name}")

        self.deck = Deck()  # deck is created here; deck knows how, games decides when
        self.deck.shuffle()  # object.method() - games gets the shuffle ability from deck.py

        # Access each player by "for player in players" loop OR by indexing
        players = self.create_players()
        turn_list = self.start_game(players)

        game_running = True  # logic is needed to state when the game ends
        while game_running:
            for player in turn_list:
                player.isTurn = True
                print(f"\n{player.name}'s turn")
                print(player.name)

                player.isTurn = True
                print(f"\n{player.name}'s turn")
                # for each player in the turn list:
                # that player takes a turn
                if (self.dealer.deck.size) == 0:
                    print("Draw pile is empty. Cannot pick up new cards.")
                else:
                    while True:
                        choice = input("Do you want to draw a card? (y/n)").lower()
                        if choice == "y":
                            card = self.dealer.deck.getCard()
                            player.hand.append(card)  # we're assuming the player has a hand
                            print(f"You drew: {card}")
                            break
                        elif choice == "n":
                            break
                        else:
                            print("Invalid input. Please enter 'y' or 'n'.")

                # end of player's turn
                player.isTurn = False

        input("Press [Enter] to exit.")

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
