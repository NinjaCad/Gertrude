from cardgames.Deck import Deck
from cardgames.Dealer import Dealer
from cardgames.Player import Player


class Games:
    
    def __init__(self, input_func=input):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.players = []
        self.input_func = input_func

        self.match_format = 1   

        self.num_rounds = self.match_format
        self.cards_per_turn = 3
        self.mode_locked = False

        
        self.num_rounds = self.match_format

        # NEW: match format
        self.match_format = 1
        self.cards_per_turn = 3

    def get_valid_input(self, prompt, min_val, max_val):
        while True:
            try:
                choice = int(self.input_func(prompt))
                if min_val <= choice <= max_val:
                    return choice
                else:
                    print(f"Error: Choice must be between {min_val} and {max_val}.")
            except ValueError:
                print("Error: Please enter a valid whole number (e.g., 1, 2, 3).")

    # =====================================================
    # GAME MODE SETUP (UPDATED)
    # =====================================================
    def setup_gamemode(self):
        print("\n--- Game Configuration ---")

        # Players
        num_players = self.get_valid_input(
            "Choose number of players (1-3): ", 1, 3
        )
        self.players = [Player(f"Player {i+1}") for i in range(num_players)]

        # FIXED RULE: always 3 cards
        self.cards_per_turn = 3
        print("Cards per turn locked: 3 (choose 1 out of 3 cards).")

        # MATCH FORMAT
        self.match_format = self.get_valid_input(
            "Choose match format (1 = BO1, 3 = BO3, 5 = BO5): ", 1, 5
        )

        if self.match_format not in [1, 3, 5]:
            print("Invalid format. Defaulting to Best of 3.")
            self.match_format = 3

        print(
            f"\nGame set:\n"
            f"- Players: {len(self.players)}\n"
            f"- Cards per turn: {self.cards_per_turn}\n"
            f"- Match format: Best of {self.match_format}\n"
        )

    def preview_deck(self):
        print("\nFirst 5 cards in standard 52-card deck:")
        for card in self.deck.cards[:5]:
            print(card)

    # =====================================================
    # MAIN GAME LOOP (BEST OF SYSTEM)
    # =====================================================
    def run_game(self):
        print("Welcome to the Card Game Application!")

        self.preview_deck()
        self.setup_gamemode()

        wins = {p.name: 0 for p in self.players}
        ties = 0

        win_needed = (self.match_format // 2) + 1

        round_num = 0

        while True:
            round_num += 1
            print(f"\n=== Round {round_num} ===")

            self.dealer.resetDeck()

            # deal cards
            for p in self.players:
                p.clearHand()
                self.dealer.dealCards(self.cards_per_turn, [p])

                print(f"\n{p.name}, choose 1 card:")
                p.showHand(printShort=True)

                choice = self.get_valid_input("Pick card 1-3: ", 1, 3)

                selected = p.hand[choice - 1]
                p.chosen_card = selected

                print(f"You selected: {selected.value} of {selected.suit}")

            # =========================
            # SAFE WIN LOGIC
            # =========================
            p1, p2 = self.players[0], self.players[1]

            print("\n--- RESULT ---")

            if p1.chosen_card is None and p2.chosen_card is None:
                print("Both players timed out!")
                ties += 1
                continue

            if p1.chosen_card is None:
                print(f"{p1.name} timed out. {p2.name} wins!")
                wins[p2.name] += 1
                continue

            if p2.chosen_card is None:
                print(f"{p2.name} timed out. {p1.name} wins!")
                wins[p1.name] += 1
                continue

            # compare cards safely
            if p1.chosen_card.value > p2.chosen_card.value:
                print(f"{p1.name} wins the round!")
                wins[p1.name] += 1
            elif p2.chosen_card.value > p1.chosen_card.value:
                print(f"{p2.name} wins the round!")
                wins[p2.name] += 1
            else:
                print("Round is a tie!")
                ties += 1

            # =========================
            # STATS DISPLAY
            # =========================
            print("\n--- STATS ---")
            for p in self.players:
                print(f"{p.name}: {wins[p.name]} wins")
            print(f"Ties: {ties}")

            # =========================
            # CHECK MATCH WINNER
            # =========================
            for p in self.players:
                if wins[p.name] >= win_needed:
                    print(f"\n🏆 {p.name} WINS THE MATCH!")
                    return

            if round_num >= self.match_format:
                print("\nMatch ended!")
                return

    def main(self):
        self.run_game()
        self.input_func("Press [Enter] to exit.")


if __name__ == "__main__":
    game = Games()
    game.main()