from cardgames.Games import *

def main(self, test_mode= False):
    print('Welcome to High Card Draw!')
    print(HighCardDrawInstructions.get("overview"))
    input('\nPress [Enter] to start...')

    # initiate variables
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

    self.show_betting_popup(player1.name)

    # swap turn function
    end_turn = input("\nPress [Enter] to end your turn: ")
    if end_turn == "":
        player1.clear_screen()
        
    while True:
        begin = input("\nIt is now Player 2's turn! Press [Enter] to begin!")
        if begin == "":
            break
        else:
            print(f"Error: You pressed '{begin}'. Please press ONLY the [Enter] key.")
        
    dealer.dealCards(3, [player2])
    self.select_card(player2)

    self.show_betting_popup(player2.name)

    end_turn = input("\nPress [Enter] to end your turn: ")
    if end_turn == "":
        player2.clear_screen()

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
            
            # Break the loop now that we have a valid result
            break
        else:
            # Error feedback for anything other than Enter
            print(f"Invalid input: '{display_winner}'. Please press the [Enter] key only.")

    # Return the state after the loop is finished
    return player1, player2, deck

if __name__ == "__main__":
    game = Games()
    game.main(test_mode=False)