import random
from cardgames.Player import Player

# Proof of concept
# FUTURE FEATURES:
# -limit number of players

# Player creation
def create_players(numPlayers, playerNames):
     # List of Players
    positions = random.sample(range(numPlayers), numPlayers)
    players = []
    for i in range(numPlayers):
        angle = positions[i] * (360/numPlayers)
        players.append(Player(playerNames[i], angle))

    # This will be placed into the overall deck eventually
    cardsLeft = 52 % numPlayers

    return players, cardsLeft

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

    playerNames = []
    for i in range(numPlayers):
        name = input(f"Enter a player name ({i+1}/{numPlayers}): ")
        playerNames.append(name)

    players, cardsLeft = create_players(numPlayers, playerNames)

    return playerNames, numPlayers

if __name__ == "__main__":
    start_game()