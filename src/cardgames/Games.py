from cardgames.Player import *
from cardgames.Deck import *
from cardgames.Card_Compare import *
from cardgames.Deck import *
from cardgames.betting_templates import *
from cardgames.Player import *
from cardgames.Dealer import *
import copy

# ==========================================================
# New Feature (Sprint 1): High Card Draw instructions display
# ==========================================================

class HighCardDrawInstructions:
    """Rules/instructions provider for the High Card Draw game.

    The design goal is to keep display/UI separate from the rules text.
    Callers can print the returned strings or show them in any UI.
    """

    GAME_KEY = "high_card_draw"

    # two topics plus validation.
    _TOPICS = {
        "overview": (
            "\nHigh Card Draw is a 2-player, 1-round game. \n\nEach player is dealt 3 cards, "
            "chooses 1 card in secret, then both cards are revealed at the same time."
            "\n\nNote: Clubs are higher than Diamonds, which are higher than Hearts, which are higher than Spades!"
        ),
        "winning": (
            "Winning:\n"
            "- Higher card value wins the round.\n"
            "- If values tie, the round is a tie (unless your team adds a tiebreaker)."
        ),
    }

    @classmethod
    def topics(cls) -> list[str]:
        """Return a sorted list of available instruction topics."""
        return sorted(cls._TOPICS.keys())

    @classmethod
    def get(cls, topic: str = "overview") -> str:
        """Get formatted High Card Draw instructions for a specific topic.

        Args:
            topic: One of: 'overview', 'winning'

        Returns:
            A formatted multi-line string suitable for printing.

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
        
def declare_winner(player1, player2):
        card1 = player1.chosen_card
        card2 = player2.chosen_card
        try:
            if card1.compare(card2)==1: # player1 wins
                return player1.name
            elif card1.compare(card2)==-1: # player2 wins
                return player2.name
            elif card1.compare(card2)==0:
                return "It's a tie!"
        except TypeError: # tie
            print("Error: Both players must have chosen a card to declare a winner.")

class Games:

    def __init__(self):
        self.deck = Deck()

    def select_card(self, player):
        # Denotes the change of turn 
        print(f"\n--- {player.name}'s Card Options ---")
        if len(player.hand) == 0: # Added by Sam's suggestion
            print(f"{player.name} has no cards left to play!")
            player.chosen_card = None  # Intentionally set to None since player cannot pick a card
            return 

        for i, card in enumerate(player.hand):
            print("\n" + show_cards(card))
        
        while True:
            try:
                max_choice = len(player.hand)
                # Prompting player to pick a card
                choice = int(input(f"Select one of the cards to play (1-{max_choice}): "))
                
                # Check if choice is valid
                if 1 <= choice <= max_choice:
                    # Assign the chosen card using player.hand
                    player.chosen_card = player.hand[choice - 1]
                    print(f"\nGreat! You selected \n\n{show_cards(player.chosen_card)}.")
                    break 
                else:
                    # error handling in case they pick a number outside the options
                    print(f"Invalid choice. Please pick a number between 1 and {max_choice}.")
                    
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def build_betting_notification(self, chosen_player_name):
        template = random.choice(gambling_templates)
        return template.format(player=chosen_player_name)

    def show_betting_popup(self, chosen_player_name):
        """Print a popup-style betting message and return it for testability."""
        message = self.build_betting_notification(chosen_player_name)
        popup = f"\n[BETTING POP-UP] {message}"
        print(popup)
        return message

    def main(self, test_mode=False):
        # Initialize players and stats
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        game_stats = None # Starts empty, will be updated by get_game_stats

        player1.clear_screen()
        print('\nWelcome to High Card Draw!\n')
        print(HighCardDrawInstructions.get("\noverview\n"))
        input('\n------Press [Enter] to start------')

        while True:
            # Re-shuffle deck for every new round
            deck = Deck()
            deck.shuffle()
            dealer = Dealer(deck)
            
            # Clear hands from previous round
            player1.hand = []
            player2.hand = []

            # --- Player 1 Turn ---
            while True:
                begin = input("\nIt is now Player 1's turn! Press [Enter] to begin!")
                if begin == "": break
                print(f"Error: Please press ONLY the [Enter] key.")
            
            dealer.dealCards(3, [player1])
            self.select_card(player1)
            self.show_betting_popup(player1.name)

            input("\nPress [Enter] to end your turn: ")
            player1.clear_screen()

            # --- Player 2 Turn ---
            while True:
                begin = input("\nIt is now Player 2's turn! Press [Enter] to begin!")
                if begin == "": break
                print(f"Error: Please press ONLY the [Enter] key.")
            
            dealer.dealCards(3, [player2])
            self.select_card(player2)
            self.show_betting_popup(player2.name)

            input("\nPress [Enter] to end your turn: ")
            player2.clear_screen()

            # --- Display Winner & Update Stats ---
            while True:
                display_winner = input("\nPress [Enter] to display the winner!")
                if display_winner == "": break
                else:
                    print("Please press ONLY the [Enter] key.")
            winner = declare_winner(player1, player2)
            print("-" * 30)
            print(f"THE WINNER IS: {winner}")
            print("-" * 30)
            print(f"Player 1 chose:\n{player1.chosen_card}")
            print(f"Player 2 chose:\n{player2.chosen_card}")
            
        
            # Update game_stats and pass it back into the function next time
            game_stats = self.get_game_stats(str(winner), [player1.name, player2.name], game_stats)
            self.display_game_stats(game_stats)

            # --- The "Play Again" Logic ---
            while True:
                user_input = input("\nPress [Enter] to play again, or type 'exit' to finish: ")

                if user_input == "":
                    break

                elif user_input.lower().strip() == "exit":
                    print("\nThanks for playing High Card Draw! Final stats shown above.\n")
                    return player1, player2, deck

                else:
                    print(f"Error: You pressed '{user_input}', please ONLY press [Enter] or 'exit'")

    def get_game_stats(self, winner: str, players: list, game_stats=None):
        # Below is for every time a game has been ran
        # Set up game_stats dict if it is empty
        if game_stats == None:
            game_stats = {}
            for player in players:
                game_stats[player] = {}
                game_stats[player]["Wins"] = 0
                game_stats[player]["Win-Rate"] = ""
                game_stats[player]["Win Streak"] = 0
                game_stats[player]["Highest Win Streak"] = 0
            game_stats["Ties"] = 0
            game_stats["Total Games"] = 0
        
        # Error handling
        game_stats = copy.deepcopy(game_stats)
        keys = list(game_stats.keys())
        if winner not in keys and winner != "It's a tie!":
            raise ValueError("Invalid winner")
        for player in players:
            if player not in keys:
                raise ValueError("Player not found")

        # Increment the number of wins or ties
        if winner == "It's a tie!":
            game_stats["Ties"] += 1

            # Every player loses their win streak if it's a tie
            for player in players:
                game_stats[player]["Win Streak"] = 0
        else:
            game_stats[winner]["Wins"] += 1

            # Update winner's win streak and highest win streak
            game_stats[winner]["Win Streak"] += 1
            if game_stats[winner]["Win Streak"] > game_stats[winner]["Highest Win Streak"]:
                game_stats[winner]["Highest Win Streak"] = game_stats[winner]["Win Streak"]

            # Reset everyone else's win streak
            for player in players:
                if player != winner:
                    game_stats[player]["Win Streak"] = 0

        # Total games is the sum of Player1 wins, Player2 wins, and ties
        total_games = 0
        for player in players:
            total_games += game_stats[player]["Wins"]
        total_games += game_stats["Ties"]
        game_stats["Total Games"] += 1

        #Calculate and update the win rate for both players
        for player in players:
            win_rate = game_stats[player]["Wins"] / total_games * 100
            value = f"{win_rate:.1f}" + "%"
            game_stats[player]["Win-Rate"] = value

        return game_stats
    
    def display_game_stats(self, game_stats):
        print("-"*30)
        print("Game Statistics")
        print("-"*30)
        print(f"Total Games Played: {game_stats['Total Games']}\n")
        print("          | Wins | Win Rate | Current Win Streak | Highest Win Streak |")
        for player, stats in game_stats.items():
            if not isinstance(stats, dict):
                continue
            # For when iterating over "Ties" and "Total Games"

            wins = stats['Wins']
            winrate = stats['Win-Rate']
            win_streak = stats['Win Streak']
            high_win_streak = stats['Highest Win Streak']
            print(f"{player:9} | {wins:4} | {winrate:8} | {win_streak:18} | {high_win_streak:18} |")
        ties = game_stats['Ties']
        print(f"\nTies: {ties}")

if __name__ == "__main__":
    game = Games()
    game.main(test_mode=False)

    # Adjustments
    """

    3. Player profiles?
    print chosen cards

    """
