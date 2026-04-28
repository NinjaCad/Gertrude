from testing_base import *

def test_cardSteal():
    queen = [""," _____ ", "|Q  ww|", "| ^ {(|", "|(.)%%|", "| |%%%|", "|_%%%O|"]
    king = [" _____ ", "|K  WW|", "| ^ {)|", "|(.)%%|", "| |%%%|", "|_%%%>|"]
    ace = [" _____ ","|A .  |","| /.  |","|(_._)|","|  |  |","|____V|"]
    two = [" _____ ","|2    |","|  ^  |","|     |","|  ^  |","|____Z|"]
    three = [" _____ ","|3    |","| ^ ^ |","|     |","|  ^  |","|____E|"]

    cards = [
        Card("Spades", 12, queen, queen),   # Queen
        Card("Hearts", 2, two, two),    # two
        Card("Clubs", 13, king, "|K  WW|"),    # King
        Card("Diamonds", 3, three, "|3    |"),  # three
        Card("Clubs", 1, ace, "|A _  |"),     # ace
    ]

    game = Games()
    Dory = Player("Dory") #Main Player
    Marlin = Player("Marlin")
    Nemo = Player("Nemo")
    FishThatAteNemosFamily = Player("ThatGuy")

    players = [Marlin, Dory, Nemo, FishThatAteNemosFamily]
    Dory.hand = [cards[0],cards[1],cards[2],cards[3],cards[4]]
    Marlin.hand = [cards[0],cards[0],cards[0],cards[0],cards[0]] #Test Marlin for multiple cards (QUEEN)
    Nemo.hand = [cards[0],cards[1],cards[2],cards[3],cards[4]] #Test Nemo for Mix of cards
    FishThatAteNemosFamily.hand = [cards[0],cards[1],cards[2],cards[3],cards[0]] #test lack of (ACE)


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
    

    targeted_player = game.card_thievery(Dory, players)

    print("")
    print("Dory's Hand:")
    print(len(Dory.hand))
    while len(Dory.hand) > 5:
        print(Dory.hand[len(Dory.hand) - 1])
        Dory.removeCard(Dory.hand[len(Dory.hand) - 1])
    print("\n")

test_cardSteal()
