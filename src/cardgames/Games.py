from cardgames.Deck import Deck
from cardgames.Dealer import Dealer
from cardgames.Player import Player
from cardgames.Time_limit import player_choose_card_timed
from cardgames.Card_Compare import Card
from cardgames.betting_templates import gambling_templates
from cardgames.declare_winner import *
import random

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


class Games:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.players = [Player("Player 1"), Player("Player 2")]

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

    def main(self, test_mode= False):
        print('Welcome to High Card Draw!')
        print(HighCardDrawInstructions.get("overview"))
        input('\nPress [Enter] to start...')

        # initiate variables
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        deck = Deck()
        deck.shuffle()
        dealer = Dealer(deck)

        while True:
            begin = input("\nIt is now Player 1's turn! Press [Enter] to begin!")
            if begin == "":
                break
            else:
                print(f"Error: You pressed '{begin}'. Please press ONLY the [Enter] key.")
        
        dealer.dealCards(3, [player1])
        self.select_card(player1)

        self.show_betting_popup(player1.name)

        # swap turn function
        while True:
            end_turn = input("\nPress [Enter] to end your turn: ")
            if end_turn == "":
                player1.clear_screen()
                break
            else:
                print(f"Error: You pressed '{end_turn}'. Please press ONLY the [Enter] key.")
        
        while True:
            begin = input("\nIt is now Player 2's turn! Press [Enter] to begin!")
            if begin == "":
                break
            else:
                print(f"Error: You pressed '{begin}'. Please press ONLY the [Enter] key.")
        
        dealer.dealCards(3, [player2])
        self.select_card(player2)

        self.show_betting_popup(player2.name)

        while True:
            end_turn = input("\nPress [Enter] to end your turn: ")
            if end_turn == "":
                player2.clear_screen()
                break
            else:
                print(f"Error: You pressed '{end_turn}'. Please press ONLY the [Enter] key.")

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

        while True:
            display_winner = input("\nPress [Enter] to display the winner: ")
        
            if display_winner == "":
                # Call the function and store the result
                winner = declare_winner(player1, player2)
            
                # Display results
                print("-" * 30)
                print(f"THE WINNER IS: {winner}")
                print("-" * 30)
                print(f"\n{player1.name} chose: \n{player1.chosen_card}")
                print(f"\n{player2.name} chose: \n{player2.chosen_card}")
                print("\n" + "-" * 30)
            
                # Break the loop now that we have a valid result
                break
            else:
                # Error feedback for anything other than Enter
                print(f"Invalid input: '{display_winner}'. Please press the [Enter] key only.")

        # Return the state after the loop is finished
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
            else:
                print("It's a tie!")

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

if __name__ == "__main__":
    game = Games()
    game.main()