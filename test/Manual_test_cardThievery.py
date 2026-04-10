from testing_base import *

def test_cardSteal():
    queen = [" _____ ", "|Q  ww|", "| ^ {(|", "|(.)%%|", "| |%%%|", "|_%%%O|"]
    king = [" _____ ", "|K  WW|", "| ^ {)|", "|(.)%%|", "| |%%%|", "|_%%%>|"]
    ace = [" _____ ","|A .  |","| /.  |","|(_._)|","|  |  |","|____V|"]
    two = [" _____ ","|2    |","|  ^  |","|     |","|  ^  |","|____Z|"]
    three = [" _____ ","|3    |","| ^ ^ |","|     |","|  ^  |","|____E|"]
    back = [" _____ ","|/ ~ /|","|}}:{{|","|}}:{{|","|}}:{{|","|/_~_/|"]

    cards = [
        Card("Spades", 12, queen, back),   # Queen
        Card("Hearts", 2, two, back),    # two
        Card("Clubs", 13, king, back),    # King
        Card("Diamonds", 3, three, back),  # three
        Card("Clubs", 1, ace, back),     # ace
    ]

    for card in cards:
        card.shortImage = back

        

    game = Games()
    Dory = Player("Dory") #Main Player
    Marlin = Player("Marlin")
    Nemo = Player("Nemo")
    FishThatAteNemosFamily = Player("ThatGuy")

    players = [Marlin, Dory, Nemo, FishThatAteNemosFamily]
    Dory.setHand([cards[0], cards[1], cards[2], cards[3], cards[3]], isKnown=True)
    Marlin.setHand([cards[0], cards[0], cards[1], cards[1], cards[0]], isKnown=True) #Test stealing queen multiples
    Nemo.setHand([cards[0], cards[1], cards[2], cards[3], cards[4]], isKnown=True) #Test stealing singles
    FishThatAteNemosFamily.setHand([cards[0], cards[1], cards[2], cards[3], cards[0]], isKnown=True)

    


    #Put in names or player numbers, anything printed should work.
    #Put in Letters, words, etc, it should come up as an Error

    #Select card type, eg aces or queen, those should work.
    #put in incorrect input to make sure no errors come up
    #make sure go fish only happens when card is stolen.
    #Check Print to make sure stolen card is of correct type.

    #Test for multiple stolen card, check if same type.
    #If card is not the same as chosen, check if Go Fish.

    #Test Marlin for multiple cards (QUEEN)
    #Test Nemo for Mix of cards
    #Test ThatGuy (Fish that ate nemos family) for lack of an ace. (go fishing.)
    

    notGoneFishing = game.card_thievery(players, Dory)

    print("")
    print("Dory's Hand:")
    print(len(Dory.hand))
    if notGoneFishing:
        while len(Dory.hand) > 5:
            print(Dory.hand[len(Dory.hand) - 1])
            Dory.removeCard(Dory.hand[len(Dory.hand) - 1])

test_cardSteal()
