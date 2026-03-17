from testing_base import *

def test_cardsteal():
    deck = Deck()
    dealer = Dealer(deck)

    game = Games()
    Dory = Player("Dory")
    Marlin = Player("Marlin")
    Nemo = Player("Nemo")
    FishThatAteNemosFamily = Player("ThatGuy")

    players = [Marlin, Dory, Nemo, FishThatAteNemosFamily]

    #Put in numbers higher than the amount of players,
    #Put in Letters, words, etc
    #All should come up as an Error
    #Put in number according to player, should work.

    #Select card between 0 and 5 for players hand, anything higher or below should not work.
    #Words should not work. Temporary use of numbers until card ids.

    dealer.dealCards(5, players)
    targeted_player = game.card_thievery(players, Dory)

    print("")
    print("Dory's Hand:")
    print(len(Dory.hand))
    print("Target's Hand:")
    print(len(targeted_player.hand))

test_cardsteal()
