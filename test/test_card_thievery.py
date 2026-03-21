from testing_base import *

def test_cardsteal():
    deck = Deck()
    deck.shuffle() #shuffled so that we can get duplicates

    game = Games()
    Dory = Player("Dory")
    Marlin = Player("Marlin")
    Nemo = Player("Nemo")
    FishThatAteNemosFamily = Player("ThatGuy")

    players = [Marlin, Dory, Nemo, FishThatAteNemosFamily]

    #Put in names or player numbers, anything printed should work.
    #Put in Letters, words, etc, it should come up as an Error

    #Select card type, eg aces or queen, those should work.
    #put in incorrect input to make sure no errors come up
    #make sure go fish only happens when card is stolen.
    #Check Print to make sure stolen card is of correct type.

    #Test for multiple stolen card, check if same type.

    for unit in range(10):
        for player in players:
            player.addCard(deck.getCard())

    targeted_player = game.card_thievery(players, Dory)

    print("")
    print("Dory's Hand:")
    print(len(Dory.hand))
    if len(Dory.hand) == 11:
        print(str(Dory.hand[len(Dory.hand) - 1]))
    if len(Dory.hand) > 11:
        print(str(Dory.hand[len(Dory.hand) - 1]))
        print(str(Dory.hand[len(Dory.hand) - 2]))
    print("Target's Hand:")
    print(len(targeted_player.hand))

test_cardsteal()
