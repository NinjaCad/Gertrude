from testing_base import *

def test_gofish():
    game = Games()
    king_image = [" _____ ", "|K  WW|", "| ^ {)|", "|(.)%%|", "| |%%%|", "|_%%%>|"]
    king_card = [Card("Clubs", 13, king_image, "|K  WW|")]
    
    Marlin = Player("Marlin")
    while len(Marlin.hand) < 3:
        Marlin.addCard(king_card[0])
    print("Marlin's Cards: "+str(len(Marlin.hand)))
    card = game.goFishing(Marlin)
    print("\n Marlin's Cards: "+str(len(Marlin.hand)))

    #Test for when player has book for recursive draw
    assert len(Marlin.hand) == 4 #Books will be handled by Player Turn function.

    Nemo = Player("Nemo")
    while len(Nemo.hand) < 2:
        Nemo.addCard(king_card[0])
    print("Nemo's Cards: "+str(len(Nemo.hand)))
    card = game.goFishing(Nemo)
    print("\n Nemo's Cards: "+str(len(Nemo.hand)))

    assert len(Nemo.hand) == 3 

test_gofish()