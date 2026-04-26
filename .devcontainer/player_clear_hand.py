from testing_base import *


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.knownCards = []

    def addCard(self, card, isKnown=True):
        self.hand.append(card)
        if isKnown:
            self.knownCards.append(True)
        else:
            self.knownCards.append(False)
    def clearHand(self):
        self.hand = []
        self.knownCards = []

p = Player("Test")
p.addCard("Card A", isKnown=True)
p.addCard("Card B", isKnown=False)

print(f"Start: Hand has {len(p.hand)} items.")

p.clearHand()

if len(p.hand) == 0 and len(p.knownCards) == 0:
    print("SUCCESS: Hand is empty.")
else:
    print("FAIL: Hand is not empty.")








dealer.dealCards(5, [player])

if len(player.hand) == 5 and len(player.knownCards) == 5:
    print("Setup Successful: Player has 5 cards.")
else:
    print("Setup Failed!")

player.clearHand()

if len(player.hand) == 0 and len(player.knownCards) == 0:
    print("SUCCESS: Hand and KnownCards are both size 0.")
else:
    print(f"FAILURE: Hand size is {len(player.hand)}")
    
if isinstance(player.hand, list):
    print("SUCCESS: Hand is still a list object.")
else:
    print("FAILURE: Hand is no longer a list!")