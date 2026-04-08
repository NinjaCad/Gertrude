from cardgames.Deck import Deck
from cardgames.Dealer import Dealer
from cardgames.Player import Player
from Time_limit import player_choose_card_timed

class Games:
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer(self.deck)
        self.players = [Player("Player 1"), Player("Player 2")]

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

        # 4. CLEANUP for next round
        for p in self.players:
            p.clearHand()

if __name__ == "__main__":
    game = Games()
    game.main()