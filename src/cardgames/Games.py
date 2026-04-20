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
                print("It's a tie!")
                return "It's a tie!"

    def get_game_stats(self, winner: str, players: list, game_stats=None):
        if game_stats is None:
            game_stats = {}
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