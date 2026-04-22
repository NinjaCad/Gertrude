<<<<<<< HEAD
=======
from cardgames.Deck import Deck
from cardgames.Dealer import Dealer
from cardgames.Player import Player
from cardgames.Time_limit import player_choose_card_timed
from cardgames.Card_Compare import Card
from cardgames.betting_templates import gambling_templates
import random

>>>>>>> origin/dev_backrow_buggers
import copy
from cardgames.Deck import Deck
from cardgames.Dealer import Dealer
from cardgames.Player import Player
from cardgames.Card_Compare import Card
from Time_limit import player_choose_card_timed


def show_cards(card: Card):
    face_names = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
    card_name = face_names.get(card.value, card.value)

    display_text = f"--- {card_name} of {card.suit} ---\n"

    for line in card.image:
        display_text += line + "\n"

    return display_text


class HighCardDrawInstructions:
    GAME_KEY = "high_card_draw"

    _TOPICS = {
        "overview": (
            "High Card Draw is a 2-player game. Each player is dealt 3 cards, "
            "chooses 1 card in secret, then both cards are revealed."
        ),
        "winning": (
            "Higher card value wins. If equal, it's a tie."
        ),
    }

    @classmethod
    def topics(cls):
        return sorted(cls._TOPICS.keys())

    @classmethod
    def get(cls, topic="overview"):
        topic = (topic or "overview").lower().strip()
        if topic not in cls._TOPICS:
            raise ValueError(f"Invalid topic: {topic}. Valid: {cls.topics()}")

        return f"""
=============================
{cls.GAME_KEY.upper()} - {topic.upper()}
=============================
{cls._TOPICS[topic]}
""".strip()


<<<<<<< HEAD
def declare_winner(player1, player2):
    card1 = player1.chosen_card
    card2 = player2.chosen_card

    try:
        if card1.compare(card2) == 1:
            return player1.name
        elif card1.compare(card2) == -1:
            return player2.name
        elif card1.compare(card2) == 0:
            return "It's a tie!"
    except TypeError:
        print("Error: Both players must have chosen a card to declare a winner.")
=======
        Raises:
            ValueError: if topic is unknown.
        """
        topic_key = (topic or "overview").strip().lower()
        if topic_key not in cls._TOPICS:
            valid = ", ".join(cls.topics())
            raise ValueError(f"Unknown topic '{topic}'. Valid topics: {valid}")

        title = f"{cls.GAME_KEY}: {topic_key}".upper()
        bar = "=" * len(title)
        return f"{bar}\n{title}\n{bar}\n{cls._TOPICS[topic_key]}"

def show_cards(card: Card):
        face_names = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
        card_name = face_names.get(card.value, card.value)
        
        display_text = f"--- {card_name} of {card.suit} ---\n"
        
        for line in card.image:
            display_text += line + "\n"
            
        return display_text
>>>>>>> origin/dev_backrow_buggers


class Games:
    

    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.players = []
        self.num_rounds = 1
        self.cards_per_turn = 3
        self.mode_locked = False

    # =====================================================
    # ONLY CHANGE: setup_gamemode UPDATED (BEST OF SYSTEM)
    # =====================================================
    def setup_gamemode(self):
        """Game setup locked to High Card Draw rules."""

        print("\n--- Game Configuration ---")

        # Players locked to 2
        num_players = 2
        print("Players locked: 2 players")

        self.players = [Player(f"Player {i+1}") for i in range(num_players)]

        # FIXED RULE: always 3 cards per turn
        self.cards_per_turn = 3
        print("Cards per turn locked: 3 (choose 1 out of 3 cards).")

        # NEW: Best of system (1 / 3 / 5)
        while True:
            try:
                mode = int(input("Choose match format (1 = BO1, 3 = BO3, 5 = BO5): "))
                if mode in [1, 3, 5]:
                    self.num_rounds = mode
                    break
                else:
                    print("Error: Must be 1, 3, or 5.")
            except ValueError:
                print("Error: Please enter a valid number.")

        self.mode_locked = True

        print(
            f"\nGame set:\n"
            f"- Players: {len(self.players)}\n"
            f"- Cards per turn: {self.cards_per_turn}\n"
            f"- Match format: Best of {self.num_rounds}\n"
        )

<<<<<<< HEAD
    def main(self):
        print('Welcome to High Card Draw!')

        self.setup_gamemode()

        game_stats = None

        for round_num in range(1, self.num_rounds + 1):
            print(f"\n{'='*30}")
            print(f"         ROUND {round_num} of {self.num_rounds}")
            print(f"{'='*30}")

            self.dealer.resetDeck()

            for p in self.players:
                p.clearHand()
                self.dealer.dealCards(self.cards_per_turn, [p])
                p.setHand(p.hand, isKnown=True)

            for p in self.players:
                player_choose_card_timed(p, 10)

            winner = self.declare_winner(self.players[0], self.players[1])

            if winner is not None:
                game_stats = self.get_game_stats(
                    winner,
                    [p.name for p in self.players],
                    game_stats
                )
                self.print_stats(game_stats)

        print("\nGame Over! Thanks for playing.")

    def declare_winner(self, player1, player2):
=======
    def declare_winner(self):
>>>>>>> origin/dev_backrow_buggers
        p1, p2 = self.players[0], self.players[1]

        print("\n" + "="*30)
        print("       FINAL RESULTS")
        print("="*30)

        if p1.chosen_card is None and p2.chosen_card is None:
            print("Both players timed out! No one wins.")
            return None
        elif p1.chosen_card is None:
            print(f"{p1.name} timed out. {p2.name} wins by default!")
            return p2.name
        elif p2.chosen_card is None:
            print(f"{p2.name} timed out. {p1.name} wins by default!")
<<<<<<< HEAD
            return p1.name
        else:
            print(f"{p1.name} played:\n{p1.chosen_card}")
            print(f"{p2.name} played:\n{p2.chosen_card}")

            if p1.chosen_card.value > p2.chosen_card.value:
                print(f"*** Winner: {p1.name}! ***")
                return p1.name
            elif p2.chosen_card.value > p1.chosen_card.value:
                print(f"*** Winner: {p2.name}! ***")
                return p2.name
=======
        else:
            # Both players made a choice, compare card values
            if p1.chosen_card.value > p2.chosen_card.value:
                print(f"{p1.name} wins with {p1.chosen_card}!")
            elif p2.chosen_card.value > p1.chosen_card.value:
                print(f"{p2.name} wins with {p2.chosen_card}!")
            else:
                print("It's a tie!")
                return "It's a tie!"

# HANNAH'S CODE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def handle_ties(self, players):
        player1 = players[0]
        player2 = players[1]
        begin = input("\nIt is now Player 1's turn! Press [Enter] to begin!")
        # Player 1 chooses a card
        if begin == "":
            self.select_card(player1)
            
        # swap turn function
        end_turn = input("\nPress [Enter] to end your turn: ")
        if end_turn == "":
            player1.clear_screen()
        
        begin = input("\nIt is now Player 2's turn! Press [Enter] to begin!")
        # Player 2 chooses a card
        if begin == "":
            self.select_card(player2)
    
        end_turn = input("\nPress [Enter] to end your turn: ")
        if end_turn == "":
            player2.clear_screen()
            
    def build_betting_notification(self, chosen_player_name):
        template = random.choice(gambling_templates)
        return template.format(player=chosen_player_name)

    def show_betting_popup(self, chosen_player_name):
        """Print a popup-style betting message and return it for testability."""
        message = self.build_betting_notification(chosen_player_name)
        popup = f"\n[BETTING POP-UP] {message}"
        print(popup)
        return message

    def select_card(self, player):  # Function by Tyson
        """Denotes the change of turn"""
        print(f"\n--- {player.name}'s Turn ---")
        
        if len(player.hand) == 0:  # Added by Sam's suggestion
            print(f"{player.name} has no cards left to play!")
            player.chosen_card = None  # Intentionally set to None since player cannot pick a card
            return 

        player.showHand(printShort=True)
        
        while True:
            try:
                max_choice = len(player.hand)
                # Prompting player to pick a card
                choice = int(input(f"Select a card to play (1-{max_choice}): "))
                
                # Check if choice is valid
                if 1 <= choice <= max_choice:
                    # Assign the chosen card using player.hand
                    player.chosen_card = player.hand[choice - 1]
                    print(f"Great! You selected {player.chosen_card}.")
                    break 
                else:
                    # error handling in case they pick a number outside the options
                    print(f"Invalid choice. Please pick a number between 1 and {max_choice}.")
                    
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def main(self, test_mode= False):
        print('Welcome to High Card Draw!')
        
        if not test_mode:
            print('First 3 cards in standard 52-card deck:')
            for card in self.deck.cards[:3]:
                print(card)
            input('Press [Enter] to exit.')

            # Example usage of New Feature: instructions display.
            # This is the demo only - the rules system itself is tested through pytest.
            print("\nHigh Card Draw Instructions (overview):")
            print(HighCardDrawInstructions.get("overview"))
            input('Press [Enter] to start.')

        #  print instructions
        print(HighCardDrawInstructions.get("overview"))
        input('\nPress [Enter] to start...')

        # initiate variables
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        deck = Deck()
        deck.shuffle()
        dealer = Dealer(deck)

        begin = input("\nIt is now Player 1's turn! Press [Enter] to begin!")
        # Player 1 chooses a card
        if begin == "":
            dealer.dealCards(3, [player1])
            self.select_card(player1)
            
        # deal cards to players
        dealer.dealCards(3, [player1, player2])

        self.show_betting_popup(player1.name)
        self.show_betting_popup(player2.name)

        # display player 1's cards
        for card in player1.hand:
            print(show_cards(card))
        # player1 chooses a card
        # I am waiting for the function that allows player to choose a card
        # stand in code
        self.select_card(player1)

        # swap turn function
        end_turn = input("\nPress [Enter] to end your turn: ")
        if end_turn == "":
            player1.clear_screen()
        
        begin = input("\nIt is now Player 2's turn! Press [Enter] to begin!")
        # Player 2 chooses a card
        if begin == "":
            dealer.dealCards(3, [player2])
            self.select_card(player2)
    
        end_turn = input("\nPress [Enter] to end your turn: ")
        if end_turn == "":
            player2.clear_screen()

        display_winner = input("\nPress [Enter] to display the winner: ")
        if display_winner == "":
            # display winner
            winner = self.declare_winner()

# HANNAH'S CODE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

            while winner == "It's a tie!":
                self.handle_ties([player1, player2])
                winner = self.declare_winner()

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<

            print("\nThe winner is: ", winner)
            print("\n" + player1.name + " chose: ")
            print(player1.chosen_card)
            print("\n" + player2.name + " chose: ")
            print(player2.chosen_card, "\n")

        return player1, player2, deck


    def get_game_stats(self, winner: str, players: list, game_stats=None):
        #Below is for every time a game has been ran
        #Set up game_stats dict if it is empty
        if game_stats == None:
            game_stats = {}
            for player in players:
                game_stats[player] = {}
                game_stats[player]["Wins"] = 0
                game_stats[player]["Win-Rate"] = ""
                game_stats[player]["Win Streak"] = 0
                game_stats[player]["Highest Win Streak"] = 0
            game_stats["Ties"] = 0
        
        #Error handling
        game_stats = copy.deepcopy(game_stats)
        keys = list(game_stats.keys())
        if winner not in keys and winner != "It's a tie!":
            raise ValueError("Invalid winner")
        for player in players:
            if player not in keys:
                raise ValueError("Player not found")

        #Increment the number of wins or ties
        if winner == "It's a tie!":
            game_stats["Ties"] += 1

            #Every player loses their win streak if it's a tie
            for player in players:
                game_stats[player]["Win Streak"] = 0

        else:
            # Using the Card's __str__ method to show the card nicely
            print(f"{players[0].name} played:\n{players[0].chosen_card}")
            print(f"{players[1].name} played:\n{players[1].chosen_card}")
            
            # Compare the actual card values
            if players[0].chosen_card.value > players[1].chosen_card.value:
                print(f"*** Winner: {players[0].name}! ***")
            elif players[1].chosen_card.value > players[1].chosen_card.value:
                print(f"*** Winner: {players[1].name}! ***")
>>>>>>> origin/dev_backrow_buggers
            else:
                print("It's a tie!")
                return "It's a tie!"

<<<<<<< HEAD
    def get_game_stats(self, winner: str, players: list, game_stats=None):
        if game_stats is None:
            game_stats = {}
=======
            #Update winner's win streak and highest win streak
            game_stats[winner]["Win Streak"] += 1
            if game_stats[winner]["Win Streak"] > game_stats[winner]["Highest Win Streak"]:
                game_stats[winner]["Highest Win Streak"] = game_stats[winner]["Win Streak"]

            #Reset everyone else's win streak
>>>>>>> origin/dev_backrow_buggers
            for player in players:
                game_stats[player] = {"Wins": 0, "Win-Rate": ""}
            game_stats["Ties"] = 0

        game_stats = copy.deepcopy(game_stats)

        if winner not in game_stats and winner != "It's a tie!":
            raise ValueError("Invalid winner")

        if winner == "It's a tie!":
            game_stats["Ties"] += 1
        else:
            game_stats[winner]["Wins"] += 1

        total_games = sum(game_stats[p]["Wins"] for p in players) + game_stats["Ties"]

        for player in players:
            win_rate = (game_stats[player]["Wins"] / total_games * 100) if total_games else 0
            game_stats[player]["Win-Rate"] = f"{win_rate:.1f}%"

        return game_stats
<<<<<<< HEAD

    def print_stats(self, game_stats: dict):
        print("\n--- Current Standings ---")
        for p in self.players:
            wins = game_stats[p.name]["Wins"]
            rate = game_stats[p.name]["Win-Rate"]
            print(f"  {p.name}: {wins} win(s) | Win Rate: {rate}")
        print(f"  Ties: {game_stats['Ties']}")

=======
>>>>>>> origin/dev_backrow_buggers

if __name__ == "__main__":
    game = Games()
    game.main()