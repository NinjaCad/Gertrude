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
#

class HighCardDrawInstructions:
    """Rules/instructions provider for the High Card Draw game."""

    GAME_KEY = "high_card_draw"

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
        return sorted(cls._TOPICS.keys())

    @classmethod
    def get(cls, topic: str = "overview") -> str:
        topic_key = (topic or "overview").strip().lower()
        if topic_key not in cls._TOPICS:
            valid = ", ".join(cls.topics())
            raise ValueError(f"Unknown topic '{topic}'. Valid topics: {valid}")

        title = f"{cls.GAME_KEY}: {topic_key}".upper()
        bar = "=" * len(title)
        return f"{bar}\n{title}\n{bar}\n{cls._TOPICS[topic_key]}"


def show_cards(card: Card):
    face_names = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
    card_name = face_names.get(card.value, card.value)

    display_text = f"--- {card_name} of {card.suit} ---\n"
    for line in card.image:
        display_text += line + "\n"
    return display_text


def declare_winner(player1, player2):
    card1 = player1.chosen_card
    card2 = player2.chosen_card
    try:
        if card1.compare(card2) == 1:
            return player1.name
        if card1.compare(card2) == -1:
            return player2.name
        return "It's a tie!"
    except TypeError:
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
        message = self.build_betting_notification(chosen_player_name)
        popup = f"\n[BETTING POP-UP] {message}"
        print(popup)
        return message

    def create_player_profile(self, player_number):
        print(f"\nSet up profile for Player {player_number}")

        entered_name = input("Name: ").strip()
        name = entered_name if entered_name else f"Player {player_number}"

        entered_nickname = input("Nickname (optional): ").strip()
        nickname = entered_nickname if entered_nickname else name

        print("Choose level:")
        print("1. Beginner")
        print("2. Intermediate")
        print("3. Advanced")
        level_choice = input("Enter 1-3 (default 1): ").strip()
        levels = {"1": "Beginner", "2": "Intermediate", "3": "Advanced"}
        level = levels.get(level_choice, "Beginner")

        player = Player(name, nickname=nickname, level=level)
        print(f"Profile saved: {player.profile_display_name()} | Level: {player.level}")
        return player

    def select_card(self, player):
        print(f"\n--- {player.name}'s Turn ---")

        if len(player.hand) == 0:
            print(f"{player.name} has no cards left to play!")
            player.chosen_card = None
            return

        player.showHand(printShort=True)

        while True:
            try:
                max_choice = len(player.hand)
                choice = int(input(f"Select a card to play (1-{max_choice}): "))
                if 1 <= choice <= max_choice:
                    player.chosen_card = player.hand[choice - 1]
                    print(f"Great! You selected {player.chosen_card}.")
                    break
                print(f"Invalid choice. Please pick a number between 1 and {max_choice}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def main(self, test_mode=False):
        print("Welcome to High Card Draw!")

        if test_mode:
            player1 = Player("Player 1")
            player2 = Player("Player 2")
            deck = Deck()
            deck.shuffle()
            dealer = Dealer(deck)
            dealer.dealCards(3, [player1, player2])
            player1.chosen_card = player1.hand[0]
            player2.chosen_card = player2.hand[0]
            return player1, player2, deck

        print(HighCardDrawInstructions.get("overview"))
        input("\nPress [Enter] to start...")

        player1 = self.create_player_profile(1)
        player2 = self.create_player_profile(2)

        deck = Deck()
        deck.shuffle()
        dealer = Dealer(deck)
        self.show_betting_popup(player1.profile_display_name())
        self.show_betting_popup(player2.profile_display_name())

        winner = "It's a tie!"
        round_number = 1

        while winner == "It's a tie!":
            if round_number > 1:
                print("\nTie game! Replaying round...\n")

            player1.clearHand()
            player2.clearHand()
            player1.chosen_card = None
            player2.chosen_card = None

            if not dealer.dealCards(3, [player1, player2]):
                dealer.resetDeck()
                dealer.dealCards(3, [player1, player2])

            input(f"\n{player1.profile_display_name()}, press [Enter] to begin your turn...")
            self.select_card(player1)
            input("\nPress [Enter] to end your turn...")
            player1.clear_screen()

            input(f"\n{player2.profile_display_name()}, press [Enter] to begin your turn...")
            self.select_card(player2)
            input("\nPress [Enter] to end your turn...")
            player2.clear_screen()

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

                game_return = self.get_game_stats(str(winner), [player1.name, player2.name])
                self.display_game_stats(game_return)
            
                # Break the loop now that we have a valid result
                break
            else:
                # Error feedback for anything other than Enter
                print(f"Invalid input: '{display_winner}'. Please press the [Enter] key only.")

            


        # Return the state after the loop is finished
        return player1, player2, deck

    def get_game_stats(self, winner: str, players: list, game_stats=None):
        if game_stats is None:
            game_stats = {}
            for player in players:
                game_stats[player] = {}
                game_stats[player]["Wins"] = 0
                game_stats[player]["Win-Rate"] = ""
                game_stats[player]["Win Streak"] = 0
                game_stats[player]["Highest Win Streak"] = 0
            game_stats["Ties"] = 0
            game_stats["Total Games"] = 0

        game_stats = copy.deepcopy(game_stats)
        keys = list(game_stats.keys())
        if winner not in keys and winner != "It's a tie!":
            raise ValueError("Invalid winner")
        for player in players:
            if player not in keys:
                raise ValueError("Player not found")

        if winner == "It's a tie!":
            game_stats["Ties"] += 1
            for player in players:
                game_stats[player]["Win Streak"] = 0
        else:
            game_stats[winner]["Wins"] += 1
            game_stats[winner]["Win Streak"] += 1
            if game_stats[winner]["Win Streak"] > game_stats[winner]["Highest Win Streak"]:
                game_stats[winner]["Highest Win Streak"] = game_stats[winner]["Win Streak"]
            for player in players:
                if player != winner:
                    game_stats[player]["Win Streak"] = 0

        total_games = 0
        for player in players:
            total_games += game_stats[player]["Wins"]
        total_games += game_stats["Ties"]
        game_stats["Total Games"] += 1

        for player in players:
            win_rate = game_stats[player]["Wins"] / total_games * 100
            value = f"{win_rate:.1f}%"
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
            #For when iterating over "Ties" and "Total Games"

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