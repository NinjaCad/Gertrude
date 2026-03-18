from cardgames.Deck import Deck
from cardgames.Player import Player

class Games:

    def __init__(self):
        self.deck = Deck()

    def main(self):
        print('Welcome to the Games application!')
        print('This games application is under development.')
        
        print('First 3 cards in standard 52-card deck:')
        for card in self.deck.cards[:3]:
            print(card)
        input('Press [Enter] to exit.')

    def select_card(self, player): # Function by Tyson
        # Denotes the change of turn 
        print(f"\n--- {player.name}'s Turn ---")
        
        player.showHand(printShort=True)
        
        while True:
            try:
                max_choice = len(player.hand)
                # Prompting player to pick a card
                choice = int(input(f"Select a card to play (1-{max_choice}): "))
                
                # Check if choice is valid
                if 1 <= choice <= max_choice:
                    # Assign the chosen card using player.hand
                    player.chosen_card = player.hand[choice - 1]
                    print("Great! You selected your card.")
                    break 
                else:
                    # error handling in case they pick a number outside the options
                    print(f"Invalid choice. Please pick a number between 1 and {max_choice}.")
                    
            except ValueError:
                print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    game = Games()
    game.main()