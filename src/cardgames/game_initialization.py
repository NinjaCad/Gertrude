import random

# Proof of concept
# TO BE ADDED: 
# -list of player objects
# -limit number of players

# Game initialization loop
def start_game():
    print("Welcome to HEART ATTACK!")
    numPlayers = ""
    # Loop to get a valid number of players from user input
    while True:
        try:
            numPlayers = int(input("How many players will be joining? "))
            if numPlayers < 2:
                print("You need at least 2 players.")
            else:
                break
        except ValueError:
            print("That's not a valid number.")
    # To be replaced with list of Player objects
    # But for now, dictionary to hold player data
    players = {}
    for i in range(numPlayers):
        name = input(f"Enter a player name ({i+1}/{numPlayers}): ")
        players[name] = [0, 0]

    positions = random.sample(range(len(players)), len(players))

    # Eventually replace with list of Player objects so cards can be added to Player.hand,
    # Replacing data[1]
    for i, (name, data) in enumerate(players.items()):
        # Angle for display location when HTML is set up
        data[0] = (positions[i]) * (360/len(players)) 
        data[1] = 52 // len(players)  

    # This will be placed into the overall deck eventually
    cardsLeft = 52 % len(players)

start_game()