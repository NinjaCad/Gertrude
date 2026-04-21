import threading

def get_timed_input(prompt, timeout):
    # Initialize with a clear type hint so Pylance stays happy
    result: list = [None] 

    def timer_task():
        
        try:
            user_input = input(prompt)
            result[0] = user_input
        except EOFError:
            result[0] = None

    thread = threading.Thread(target=timer_task)
    thread.daemon = True
    thread.start()

    thread.join(timeout)
    
    if thread.is_alive():
        return "TIMEOUT"
    
    return result[0]

def player_choose_card_timed(player, seconds):
    """
    Handles the UI and validation for a player's turn.
    """
    print(f"\n--- {player.name}'s Turn ---")
    
    # Show the hand so they know what they are picking
    player.showHand(printShort=True)
    
    max_choice = len(player.hand)
    prompt = f"Select a card to play (1-{max_choice}) [{seconds}s]: "
    
    answer = get_timed_input(prompt, seconds)

    # Logic for what happens based on the timer result
    if answer == "TIMEOUT":
        print(f"\n\n{'!'*20}")
        print(f"TIME EXPIRED! {player.name} loses their turn.")
        print(f"{'!'*20}\n")
        player.chosen_card = None 
    
    elif answer is None or answer.strip() == "":
        print("No input detected. Turn forfeited.")
        player.chosen_card = None
        
    else:
        try:
            choice = int(answer)
            if 1 <= choice <= max_choice:
                player.chosen_card = player.hand[choice - 1]
                # Note: We removed the "Great!" print to avoid overlapping 
                # with the main game display as per your instructor's advice.
            else:
                print(f"Invalid choice! {choice} is not between 1 and {max_choice}.")
                player.chosen_card = None
        except ValueError:
            print(f"'{answer}' is not a valid number. Turn forfeited.")
            player.chosen_card = None