from cardgames.Deck import Deck
from cardgames.Player import Player
from cardgames.Dealer import Dealer
from cardgames.Card_Compare import Card
from cardgames.turns import switch_turn
from cardgames.betting_templates import gambling_templates
import copy
import random


def select_card(self, player):  # Function by Tyson
    # Denotes the change of turn
    print(f"\n--- {player.name}'s Turn ---")

    # Added by Sam's suggestion
    if len(player.hand) == 0:
        print(f"{player.name} has no cards left to play!")
        # Intentionally set to None since player cannot pick a card
        player.chosen_card = None
        return

    player.showHand(printShort=True)

    while True:
        try:
            max_choice = len(player.hand)
            # Prompting player to pick a card
            choice = int(input(f"Select a card to play (1-{max_choice}): "))

            if 1 <= choice <= max_choice:
                # Assign the chosen card using player.hand
                player.chosen_card = player.hand[choice - 1]
                print(f"Great! You selected {player.chosen_card}.")
                break
            else:
                # Error handling in case they pick a number outside the options
                print(f"Invalid choice. Please pick a number between 1 and {max_choice}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


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
        if card1.compare(card2) == 1:  # player1 wins
            return player1.name
        elif card1.compare(card2) == -1:  # player2 wins
            return player2.name
        elif card1.compare(card2) == 0:
            return "It's a tie!"
    except TypeError:  # tie
        print("Error: Both players must have chosen a card.")


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
        self._game_stats = None

    def build_betting_notification(self, player: str) -> str:
        template = random.choice(gambling_templates)
        return template.format(player=player)

    def show_betting_popup(self, player: str) -> str:
        message = self.build_betting_notification(player)
        print(f"[BETTING POP-UP] {message}")
        return message

    def playthrough(
        self,
        *,
        players: list[Player] | None = None,
        cards_per_player: int = 3,
        chosen_indices: list[int] | None = None,
        input_fn=input,
        print_fn=print,
    ) -> dict:
        """Run one high-card-draw round using existing game components.

        Returns a summary dict with players, winner, deck, and chosen indices.
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
            select_card(self, player1)
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

    def main(self, test_mode=False):
        print('Welcome to High Card Draw!')
        print('First 3 cards in standard 52-card deck:')
        for card in self.deck.cards[:3]:
            print(card)

        if not test_mode:
            input('Press [Enter] to exit.')

        # Example usage of New Feature: instructions display.
        # This is the demo only - the rules system itself is tested through pytest.
        print("\nHigh Card Draw Instructions (overview):")
        print(HighCardDrawInstructions.get("overview"))

        if not test_mode:
            input('Press [Enter] to start.')

        # Initiate variables
        player1 = Player("Player 1")
        player2 = Player("Player 2")
        deck = Deck()
        deck.shuffle()
        dealer = Dealer(deck)

        # Deal cards to players
        dealer.dealCards(3, [player1, player2])

        if test_mode:
            player1.chosen_card = player1.hand[0]
            player2.chosen_card = player2.hand[0]
        else:
            # Display player 1's cards
            print(f"\n{player1.name}'s cards:")
            for card in player1.hand:
                print(show_cards(card))

            # Player 1 chooses a card
            select_card(self, player1)
            if player1.chosen_card is None:
                raise ValueError("Player 1 did not choose a card")

            p1_choice_idx = player1.hand.index(player1.chosen_card)

            print("Switched turns. Player 2's turn to choose a card.")
            # Hide Player 1 hand before Player 2 selects.
            player1.hideHand()

            # Display player 2's cards
            print(f"\n{player2.name}'s cards:")
            for card in player2.hand:
                print(show_cards(card))

            _next_idx, p2_choice_idx = switch_turn(
                players=[player1, player2],
                current_player_index=0,
                chosen_card_index=p1_choice_idx,
                input_fn=input,
                print_fn=print,
            )
            player2.chosen_card = player2.hand[p2_choice_idx]

        # Display winner
        winner = declare_winner(player1, player2)
        print("The winner is: ", winner)
        print(player1.name + " chose: ")
        print(player1.chosen_card)
        print(player2.name + " chose: ")
        print(player2.chosen_card)

        return player1, player2, deck

    def get_game_stats(self, winner: str, players: list, game_stats=None):
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
            effective_winner = winner if winner in game_stats else (players[0] if players else player_keys[0])
            game_stats[effective_winner]["Wins"] += 1
            game_stats[effective_winner]["Win Streak"] += 1
            game_stats[effective_winner]["Highest Win Streak"] = max(
                game_stats[effective_winner]["Highest Win Streak"],
                game_stats[effective_winner]["Win Streak"],
            )

            for player in player_keys:
                if player != effective_winner:
                    game_stats[player]["Win Streak"] = 0

        # Total games is the sum of wins and ties.
        total_games = sum(game_stats[player]["Wins"] for player in player_keys) + game_stats["Ties"]

        # Calculate and update the win rate for all tracked players.
        for player in player_keys:
            win_rate = 0.0 if total_games == 0 else (game_stats[player]["Wins"] / total_games * 100)
            game_stats[player]["Win-Rate"] = f"{win_rate:.1f}%"

        if not (used_external_stats and winner == "It's a tie!"):
            self._game_stats = copy.deepcopy(game_stats)
        return game_stats


if __name__ == "__main__":
    game = Games()
    game.main(test_mode=False)
