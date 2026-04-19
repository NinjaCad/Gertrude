import os
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_player(num):
    # Wait for next player
    input(f"\nPlayer {num}: Press ENTER when you're ready...")

    # Clear before next player sees anything
    clear_screen()

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

    wait_for_player(num2)


if __name__ == "__main__":
    start_transition_screen(4, 5)