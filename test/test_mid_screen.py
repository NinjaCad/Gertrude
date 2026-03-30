from testing_base import * 
from cardgames.mid_screen import start_transition_screen
import time

def test_clear_inputs():
    print("(This should disappear after entering 's' and after Player 1 clicks [ENTER])", flush=True)
    if input("Press 's' to start transition screen script: ") != 's':
        print("Test aborted.")
        return
    else:
        start_transition_screen()
    print("\nTest complete.")

if __name__ == "__main__":
    test_clear_inputs()

