from cardgames.Deck import Deck
from cardgames.Dealer import Dealer
from cardgames.Player import Player


class Games:
    def __init__(self, input_func=input):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.players = []
        self.input_func = input_func

    def get_valid_input(self, prompt, min_val, max_val):
        """Standardized error handling for user numbers."""
        while True:
            try:
                choice = int(self.input_func(prompt))
                if min_val <= choice <= max_val:
                    return choice
                else:
                    print(f"Error: Choice must be between {min_val} and {max_val}.")
            except ValueError:
                print("Error: Please enter a valid whole number (e.g., 1, 2, 3).")

    def setup_gamemode(self):
        print("\n--- Game Configuration ---")

        num_players = self.get_valid_input(
            "Choose number of players (1-3): ", 1, 3
        )
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]

        cards_per_turn = self.get_valid_input(
            "Choose number of cards drawn for each turn (1-5): ", 1, 5
        )

        num_rounds = self.get_valid_input(
            "Choose how many rounds the game will last (1-10): ", 1, 10
        )

        return num_rounds, cards_per_turn

    def preview_deck(self):
        print("\nFirst 5 cards in standard 52-card deck:")
        for card in self.deck.cards[:5]:
            print(card)

    def run_game(self):
        print("Welcome to the Card Game Application!")

        # Keep your original simple feature
        self.preview_deck()

        rounds, pool_size = self.setup_gamemode()

        for r in range(1, rounds + 1):
            print(f"\n=== Round {r} ===")
            self.dealer.resetDeck()

            for p in self.players:
                p.clearHand()
                self.dealer.dealCards(pool_size, [p])

                print(f"\n{p.name}, choose 1 card from your options:")
                p.showHand(printShort=True)

                choice = self.get_valid_input(
                    f"Pick card 1-{pool_size}: ", 1, pool_size
                )
                selected = p.hand[choice - 1]

                print(f"You selected: {selected.value} of {selected.suit}")

        print("\nGame Over! Thanks for playing.")

    def main(self):
        self.run_game()
        self.input_func("Press [Enter] to exit.")


if __name__ == "__main__":
        game = Games()
        game.main()