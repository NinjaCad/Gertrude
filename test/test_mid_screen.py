from testing_base import *

def test_clear_inputs():
    print("=== PLAYER 1 TURN ===")
    secret_choice = input("Player 1, choose a secret card: ")

    print(f"\n[DEBUG] Player 1 chose: {secret_choice}")
    print("(This should disappear after clearing the screen)")
    
    start_transition_screen()

    print("=== PLAYER 2 TURN ===")
    print("If you can see Player 1's choice above, clearing FAILED.\n")

    input("Player 2, press ENTER to continue...")

    print("\nTest complete.")

if __name__ == "__main__":
    test_clear_inputs()

test_clear_inputs()