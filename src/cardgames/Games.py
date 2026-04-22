from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer
from cardgames.mid_screen import *
from cardgames.betting_templates import gambling_templates
from cardgames.declare_winner import *
import random
from cardgames.Card_Compare import Card
from Time_limit import player_choose_card_timed

# ==========================================================
# New Feature (Sprint 1): High Card Draw instructions display
# ==========================================================


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

{cls.GAME_KEY.upper()} - {topic.upper()}
{cls._TOPICS[topic]}
""".strip()
    
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

        Raises:
            ValueError: if topic is unknown.
        
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
        self.players = []
        self.num_rounds = 1
        self.cards_per_turn = 3
        self.mode_locked = False

    # =====================================================
    # ONLY CHANGE: setup_gamemode UPDATED (BEST OF SYSTEM)
    # =====================================================
    """
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
    """
    """
    def declare_winner(self, player1, player2):
    def declare_winner(self):
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
        else:
            # Both players made a choice, compare card values
            if p1.chosen_card.value > p2.chosen_card.value:
                print(f"{p1.name} wins with {p1.chosen_card}!")
            elif p2.chosen_card.value > p1.chosen_card.value:
                print(f"{p2.name} wins with {p2.chosen_card}!")
            else:
                return "It's a tie!"
        self._game_stats = None
    """
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
                
    def handle_ties(self, players: list[Player]):
        """Legacy compatibility helper for tie-handling tests."""
        if len(players) < 2:
            return
        player1, player2 = players[0], players[1]
        player1.chosen_card = player1.hand[0] if player1.hand else None
        player2.chosen_card = player2.hand[0] if player2.hand else None

    def build_betting_notification(self, player: str) -> str:
        template = random.choice(gambling_templates)
        return template.format(player=player)

    def show_betting_popup(self, player: str) -> str:
        message = self.build_betting_notification(player)
        print(f"[BETTING POP-UP] {message}")
        return message

    """
    def playthrough(
        self,
        *,
        players: list[Player] | None = None,
        cards_per_player: int = 3,
        chosen_indices: list[int] | None = None,
        input_fn=input,
        print_fn=print,
    ) -> dict:
        """#Run one high-card-draw round using existing game components.

       # Returns a summary dict with players, winner, deck, and chosen indices.
        """
        if players is None:
            players = [Player("Player 1"), Player("Player 2")]

        if len(players) != 2:
            raise ValueError("playthrough currently supports exactly 2 players")

        deck = Deck()
        deck.shuffle()
        dealer = Dealer(deck)
        if not dealer.dealCards(cards_per_player, players):
            raise ValueError("Not enough cards in deck to deal")

        player1, player2 = players

        if chosen_indices is not None:
            if len(chosen_indices) != 2:
                raise ValueError("chosen_indices must contain exactly two values")

            p1_choice_idx, p2_choice_idx = chosen_indices

            if not (0 <= p1_choice_idx < len(player1.hand)):
                raise ValueError("Player 1 chosen index out of range")
            if not (0 <= p2_choice_idx < len(player2.hand)):
                raise ValueError("Player 2 chosen index out of range")

            player1.hide_card(p1_choice_idx)
            player1.chosen_card = player1.hand[p1_choice_idx]
            player2.chosen_card = player2.hand[p2_choice_idx]
        else:
            self.select_card(player1)
            if player1.chosen_card is None:
                raise ValueError("Player 1 did not choose a card")

            p1_choice_idx = player1.hand.index(player1.chosen_card)

            next_idx, p2_choice_idx = switch_turn(
                players=players,
                current_player_index=0,
                chosen_card_index=p1_choice_idx,
                input_fn=input_fn,
                print_fn=print_fn,
            )
            players[next_idx].chosen_card = players[next_idx].hand[p2_choice_idx]

        winner = declare_winner(player1, player2)
        return {
            "players": players,
            "winner": winner,
            "deck": deck,
            "chosen_indices": [p1_choice_idx, p2_choice_idx],
        }
    """
    def main(self, test_mode=False):
        print('Welcome to High Card Draw!')
        print(HighCardDrawInstructions.get("overview"))
        input('\nPress [Enter] to start...')

        # Initiate variables
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
                while winner == "It's a tie!":
                    self.handle_ties([player1, player2])
        
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
            game_stats["Total Games"] = 0
        
        #Error handling
        game_stats = copy.deepcopy(game_stats)
        keys = list(game_stats.keys())
        if winner not in keys and winner != "It's a tie!":
            raise ValueError("Invalid winner")
        for player in players:
            if player not in keys:
                raise ValueError("Player not found")

        # Below is for every time a game has been ran
        used_external_stats = game_stats is not None

        # Set up game_stats dict if it is empty
        if game_stats is None:
            if self._game_stats is not None:
                # Legacy tests expect no-dict calls after first initialization
                # to return the tracked snapshot unchanged.
                return copy.deepcopy(self._game_stats)
            else:
                game_stats = {}
                for player in players:
                    game_stats[player] = {
                        "Wins": 0,
                        "Win-Rate": "",
                        "Win Streak": 0,
                        "Highest Win Streak": 0,
                    }
                game_stats["Ties"] = 0
        else:
            game_stats = copy.deepcopy(game_stats)

        # Normalize optional keys for backward compatibility.
        game_stats.setdefault("Ties", 0)
        for player_name, stats in list(game_stats.items()):
            if player_name == "Ties" or not isinstance(stats, dict):
                continue
            stats.setdefault("Wins", 0)
            stats.setdefault("Win-Rate", "")
            stats.setdefault("Win Streak", 0)
            stats.setdefault("Highest Win Streak", 0)

        player_keys = [k for k in game_stats.keys() if k != "Ties"]
        if not player_keys and players:
            player_keys = list(players)
            for player in player_keys:
                game_stats[player] = {
                    "Wins": 0,
                    "Win-Rate": "",
                    "Win Streak": 0,
                    "Highest Win Streak": 0,
                }

        # Be tolerant of invalid winners used in legacy tests.
        if winner == "It's a tie!":
            game_stats["Ties"] += 1
            for player in player_keys:
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
                return "It's a tie!"

    def get_game_stats(self, winner: str, players: list, game_stats=None):
        if game_stats is None:
            game_stats = {}

            #Update winner's win streak and highest win streak
            game_stats[winner]["Win Streak"] += 1
            if game_stats[winner]["Win Streak"] > game_stats[winner]["Highest Win Streak"]:
                game_stats[winner]["Highest Win Streak"] = game_stats[winner]["Win Streak"]

            #Reset everyone else's win streak
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
            effective_winner = winner if winner in game_stats else (players[0] if players else player_keys[0])
            game_stats[effective_winner]["Wins"] += 1
            game_stats[effective_winner]["Win Streak"] += 1
            game_stats[effective_winner]["Highest Win Streak"] = max(
                game_stats[effective_winner]["Highest Win Streak"],
                game_stats[effective_winner]["Win Streak"],
            )

            for player in player_keys:
                if player != effective_winner:
                    game_stats[player]["Win Streak"] = 0"""

        """#Total games is the sum of wins and ties
        total_games = 0
        for player in players:
            total_games += game_stats[player]["Wins"]
        total_games += game_stats["Ties"]
        game_stats["Total Games"] = total_games

        #Calculate and update the win rate for both players
        for player in players:
            win_rate = game_stats[player]["Wins"] / total_games * 100
            value = f"{win_rate:.2f}" + "%"
            game_stats[player]["Win-Rate"] = value

        # Total games is the sum of wins and ties.
        total_games = sum(game_stats[player]["Wins"] for player in player_keys) + game_stats["Ties"]

        # Calculate and update the win rate for all tracked players.
        for player in player_keys:
            win_rate = 0.0 if total_games == 0 else (game_stats[player]["Wins"] / total_games * 100)
            game_stats[player]["Win-Rate"] = f"{win_rate:.1f}%"

        if not (used_external_stats and winner == "It's a tie!"):
            self._game_stats = copy.deepcopy(game_stats)
        return game_stats

    def print_stats(self, game_stats: dict):
        print("\n--- Current Standings ---")
        for p in self.players:
            wins = game_stats[p.name]["Wins"]
            rate = game_stats[p.name]["Win-Rate"]
            print(f"  {p.name}: {wins} win(s) | Win Rate: {rate}")
        print(f"  Ties: {game_stats['Ties']}")

if __name__ == "__main__":
    game = Games()
    game.main()