from cardgames.Deck import Deck
<<<<<<< HEAD
from cardgames.Dealer import Dealer
from cardgames.Player import Player
from Time_limit import player_choose_card_timed
=======
<<<<<<< HEAD
from cardgames.Player import Player
from cardgames.Dealer import Dealer
from cardgames.Card_Compare import Card
from cardgames.Dealer import Dealer
from cardgames.betting_templates import gambling_templates
import random
=======
from cardgames.Card import Card
>>>>>>> feature/BB-25-game-stats-update
import copy

# ===================
# High Card Draw Game
# ===================

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
>>>>>>> 96c1c706ed905127f82872d092a86f696cffd9fd

class Games:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.players = [Player("Player 1"), Player("Player 2")]

<<<<<<< HEAD
    def main(self):
        print('Welcome to High Card Draw!')
        
        # 1. SHUFFLE AND DEAL
        self.deck.shuffle()
        for p in self.players:
            # Clear any old data and deal 3 fresh cards
            p.clearHand() 
            self.dealer.dealCards(3, [p])
            # Ensure cards are revealed so the player can see them to choose
            p.setHand(p.hand, isKnown=True) 

        # 2. SELECTION PHASE (TIMED)
        for p in self.players:
            player_choose_card_timed(p, 10)
            # Optional: Clear the screen after each player's turn 
            # so the next player doesn't see the previous choice
            # print("\n" * 30) 

        # 3. WINNER LOGIC
        self.declare_winner()

    def declare_winner(self):
        p1, p2 = self.players[0], self.players[1]
        
        print("\n" + "="*30)
        print("       FINAL RESULTS")
        print("="*30)
        
        # Check for Timeouts first
        if p1.chosen_card is None and p2.chosen_card is None:
            print("Both players timed out! No one wins.")
        elif p1.chosen_card is None:
            print(f"{p1.name} timed out. {p2.name} wins by default!")
        elif p2.chosen_card is None:
            print(f"{p2.name} timed out. {p1.name} wins by default!")
=======
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

    def main(self, test_mode= False):
        print('\nWelcome to High Card Draw!')
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
            winner = declare_winner(player1, player2)
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
>>>>>>> 96c1c706ed905127f82872d092a86f696cffd9fd
        else:
            # Using the Card's __str__ method to show the card nicely
            print(f"{p1.name} played:\n{p1.chosen_card}")
            print(f"{p2.name} played:\n{p2.chosen_card}")
            
            # Compare the actual card values
            if p1.chosen_card.value > p2.chosen_card.value:
                print(f"*** Winner: {p1.name}! ***")
            elif p2.chosen_card.value > p1.chosen_card.value:
                print(f"*** Winner: {p2.name}! ***")
            else:
                print("It's a tie!")

<<<<<<< HEAD
        # 4. CLEANUP for next round
        for p in self.players:
            p.clearHand()
=======
            #Update winner's win streak and highest win streak
            game_stats[winner]["Win Streak"] += 1
            if game_stats[winner]["Win Streak"] > game_stats[winner]["Highest Win Streak"]:
                game_stats[winner]["Highest Win Streak"] = game_stats[winner]["Win Streak"]

            #Reset everyone else's win streak
            for player in players:
                if player != winner:
                    game_stats[player]["Win Streak"] = 0

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
>>>>>>> 96c1c706ed905127f82872d092a86f696cffd9fd

if __name__ == "__main__":
    game = Games()
    game.main()