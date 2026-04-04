import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_transition_screen(num1, num2):
    # End current player's turn
    input(f"\nPlayer {num1}: Press ENTER to end your turn...")

    clear_screen()

    # Show transition screen
    print("===================================")
    print(f"          PLAYER {num2} TURN")
    print("===================================")
    print(f"\nPass the device to Player {num2}.")
    
    time.sleep(2)

    # Wait for next player
    input(f"\nPlayer {num2}: Press ENTER when you're ready...")

    # Clear before next player sees anything
    clear_screen()

start_transition_screen(4,5)