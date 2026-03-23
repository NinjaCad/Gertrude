from cardgames.Deck import Deck
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

class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')
        
        print('First 5 cards in standard 52-card deck:')
        for card in self.deck.cards[:5]:
            print(card)

        # Example usage of New Feature: instructions display.
        # This is the demo only - the rules system itself is tested through pytest.
        print("\nHigh Card Draw Instructions (overview):")
        print(HighCardDrawInstructions.get("overview"))
        input('Press [Enter] to exit.')

    def get_game_stats(self, winner, player1, player2, game_stats=None):
        #Below is for every time a game has been ran

        #Set up game_stats dict if it is empty
        if game_stats == None:
            game_stats = {}
            for player in [player1, player2]:
                game_stats[player] = {}
                game_stats[player]["Wins"] = 0
                game_stats[player]["Win-Rate"] = ""
            game_stats["Ties"] = 0

        game_stats = copy.deepcopy(game_stats)

        #Error handling
        keys = list(game_stats.keys())
        if winner not in keys and winner != "It's a tie!":
            return game_stats
        if player1 not in keys:
            return game_stats
        if player2 not in keys:
            return game_stats

        #Increment the number of wins or ties
        if winner == "It's a tie!":
            game_stats["Ties"] += 1
        else:
            game_stats[winner]["Wins"] += 1

        #Total games is the sum of Player1 wins, Player2 wins, and ties
        total_games = 0
        for player in [player1, player2]:
            total_games += game_stats[player]["Wins"]
        total_games += game_stats["Ties"]

        #Calculate and update the win rate for both players
        for player in [player1, player2]:
            win_rate = game_stats[player]["Wins"] / total_games * 100
            value = f"{win_rate:.1f}" + "%"
            game_stats[player]["Win-Rate"] = value

        return game_stats

if __name__ == "__main__":
    game = Games()
    game.main(test_mode=False)