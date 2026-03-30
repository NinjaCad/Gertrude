import os
import time

def player2_transition_screen():
    # Ask Player 1 to confirm end of turn
    input("\nPlayer 1: Press ENTER to end your turn...")

    # Clear Player 1's info
    os.system('cls' if os.name == 'nt' else 'clear')

    print("===================================")
    print("          PLAYER 2 TURN")
    print("===================================")
    print("\nPass the device to Player 2.")
    
    time.sleep(2)

    input("\nPlayer 2: Press ENTER when you're ready...")

    # Clear again before Player 2 sees anything
    os.system('cls' if os.name == 'nt' else 'clear')

player2_transition_screen()