import threading # I used threading here cuz input() can cause the timer to stop if player interacts. basicly it can't do both at once
import time
from cardgames.Player import Player 

# This is the "Engine" that will run the timer
def get_timed_input(prompt, timeout):
    
    result: list[str | None] = [None] # hold the text or none

    def timer_task(): # waits for user to type using input()
        
        result[0] = input(prompt)

    thread = threading.Thread(target=timer_task)
    thread.daemon = True
    thread.start()

    thread.join(timeout) # Main line that tells the main function if player doesnt input move on after X sec
    if thread.is_alive():
        return "TIMEOUT"
    
    return result[0]

def player_choose_card_timed(player, seconds):
    print(f"\n--- {player.name}'s Turn ---")
    
    # Use your existing showHand function to see the 3 cards
    player.showHand(printShort=True)
    
    # We ask for 1, 2, or 3 using the timer engine
    max_choice = len(player.hand)
    answer = get_timed_input(f"Select a card to play (1-{max_choice}): ", seconds)

    # 1. Handle the "Too Long" screen
    # 1. First, check if it's a timeout or empty
    if answer == "TIMEOUT" or answer is None:
        print("\n" + "!" * 45)
        print("Oops, you took too long to play, you lose this round")
        print("!" * 45 + "\n")
        player.chosen_card = None 
    
    else:
        
        # This is where you put your 1, 2, 3 
        try:
            choice = int(answer)  # Pylance will stop complaining now!
            
            if 1 <= choice <= len(player.hand):
                player.chosen_card = player.hand[choice - 1]
                print(f"Great! You selected a card.")
            else:
                print(f"Invalid choice! Pick between 1 and {len(player.hand)}.")
                player.chosen_card = None
        except ValueError:
            print("That wasn't a number! You lose this turn.")
            player.chosen_card = None