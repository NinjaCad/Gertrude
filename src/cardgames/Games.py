from Player import *
from Deck import *
from Card_Compare import *
from Deck import *
from Player import *
from Dealer import *

# ==========================================================
# New Feature (Sprint 1): High Card Draw instructions display
# ==========================================================
#

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

    def main(self, test_mode= False):
        print('Welcome to High Card Draw!')
        
        # Example usage of New Feature: instructions display.
        # This is the demo only - the rules system itself is tested through pytest.
        print("\nHigh Card Draw Instructions (overview):")
        print(HighCardDrawInstructions.get("overview"))
        if not test_mode:
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

        # display player 1's cards
        for card in player1.hand:
            print(show_cards(card))
        # player1 chooses a card
        # I am waiting for the function that allows player to choose a card
        # stand in code
        player1.chosen_card = player1.hand[0]

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
            player2.chosen_card = player2.hand[0]

        # display winner
        winner = declare_winner(player1, player2)
        print("The winner is: ", winner)
        print(player1.name+" chose: ")
        print(player1.chosen_card)
        print(player2.name+" chose: ")
        print(player2.chosen_card)

        return player1, player2, deck


if __name__ == "__main__":
    game = Games()
    game.main(test_mode=False)



