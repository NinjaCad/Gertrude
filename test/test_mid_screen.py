from ctypes.util import test
from testing_base import * 
from cardgames.mid_screen import start_transition_screen
import time

def test_clear_p1_inputs():
    print("(This should disappear after entering 's' and after Player 1 clicks [ENTER])", flush=True)
    if input("Press 's' to start transition screen script: ") != 's':
        print("Test aborted.")
        return
    else:
        start_transition_screen()
    print("\nTest complete.")

def test_keep_p2_info():
    start_transition_screen()
    print("\nThis text represents player 2's choices and should stick around until 'Test complete' prints.")
    print("\nTest complete.")

def test_remember_p1_choice():
    choice_og = "Player 1's chosen card"
    print("Player 1 chose: ", choice_og)
    print("\nThis choice should remain defined/the same after running the transition screen.")
    start_transition_screen()
    print("Player 1's choice after transition: ", choice_og)

if __name__ == "__main__":
    test_clear_p1_inputs()
    print("\n===================================")
    print("SECOND TEST")
    print("===================================")
    test_keep_p2_info()
    print("\n===================================")
    print("THIRD TEST")
    print("===================================")
    test_remember_p1_choice()

