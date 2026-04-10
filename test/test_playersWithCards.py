from testing_base import *

def test_PWC():
    queen = [""," _____ ", "|Q  ww|", "| ^ {(|", "|(.)%%|", "| |%%%|", "|_%%%O|"]
    king = [" _____ ", "|K  WW|", "| ^ {)|", "|(.)%%|", "| |%%%|", "|_%%%>|"]
    ace = [" _____ ","|A .  |","| /.  |","|(_._)|","|  |  |","|____V|"]
    two = [" _____ ","|2    |","|  ^  |","|     |","|  ^  |","|____Z|"]
    three = [" _____ ","|3    |","| ^ ^ |","|     |","|  ^  |","|____E|"]
    back = [" _____ ","|/ ~ /|","|}}:{{|","|}}:{{|","|}}:{{|","|/_~_/|"]

    cards = [
        Card("Spades", 12, queen,"|K  WW|"),   # Queen
        Card("Hearts", 2, two, "|K  WW|"),    # two
        Card("Clubs", 13, king, "|K  WW|"),    # King
        Card("Diamonds", 3, three, "|3    |"),  # three
        Card("Clubs", 1, ace, "|A _  |"),     # ace
    ]

    for card in cards:
        card.shortImage = back

    game = Games()
    Dory = Player("Dory") #Main Player
    Marlin = Player("Marlin")
    Nemo = Player("Nemo")
    FishThatAteNemosFamily = Player("ThatGuy")

    players = [Marlin, Dory, Nemo, FishThatAteNemosFamily]
    Nemo.setHand([cards[0], cards[1], cards[2], cards[3], cards[4]], isKnown=True)
    FishThatAteNemosFamily.setHand([cards[0], cards[1], cards[2], cards[3], cards[0]], isKnown=True)
    #Don't neet to set Dory and Marlins cards as they will start with 0.

    player_number, player_dict = game.playersWithCards(players)

    CurrentPlayers = []
    for number in player_number:
        CurrentPlayers.append(players[number])
    
    assert CurrentPlayers == [Nemo, FishThatAteNemosFamily]
    print("Success!")
    assert player_dict == {"nemo":2, "thatguy":3}
    print("Success!")


