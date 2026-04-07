from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer
from cardgames.betting_templates import gambling_templates
import random
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
            "High Card Draw is a 2-player, 1-round game. Each player is dealt 3 cards, "
            "chooses 1 card in secret, then both cards are revealed at the same time."
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

def show_cards(card: Card):
            face_names = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
            card_name = face_names.get(card.value, card.value)
    
            display_text = f"--- {card_name} of {card.suit} ---\n"
    
            for line in card.image:
                display_text += line + "\n"
        
            return display_text

class Games:

    def __init__(self):
        self.deck = Deck()

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

        # initiate variables
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        deck = Deck()
        deck.shuffle()
        dealer = Dealer(deck)

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
        # I am also waiting on the code to switch turns
        if not test_mode:
            switch = input("Enter 's' to switch turns: ")
            if switch == "s":
                print("Switched turns. Player 2's turn to choose a card.")
        # player2 chooses a card
        # stand in code
            for card in player2.hand:
                print(show_cards(card))
            self.select_card(player2)

        # display winner
        winner = declare_winner(player1, player2)
        print("The winner is: ", winner)
        print(player1.name+" chose: ")
        print(player1.chosen_card)
        print(player2.name+" chose: ")
        print(player2.chosen_card)

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
        else:
            game_stats[winner]["Wins"] += 1

        #Total games is the sum of Player1 wins, Player2 wins, and ties
        total_games = 0
        for player in players:
            total_games += game_stats[player]["Wins"]
        total_games += game_stats["Ties"]

        #Calculate and update the win rate for both players
        for player in players:
            win_rate = game_stats[player]["Wins"] / total_games * 100
            value = f"{win_rate:.1f}" + "%"
            game_stats[player]["Win-Rate"] = value

        return game_stats

if __name__ == "__main__":
    game = Games()
    game.main(test_mode=False)

