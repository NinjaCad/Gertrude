from cardgames.Card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.knownCards = []

    # changed addCard function to default the isKnown attrib to False, but still retain
    # some functionality if an explicit call to isKnown = True is needed for some reason.
    def addCard(self, card: Card, isKnown: bool = False):
        self.hand.append(card)
        self.knownCards.append(isKnown)

    def setHand(self, cards: "list[Card]", isKnown: bool = False):
        self.hand = cards
        # remove the following line to leave all cards in hand at their default of "isKnown = False" 
        #self.knownCards = [isKnown for _ in self.hand]

    # Removed the showHand function because there's no need for it in our game.
    # def showHand(self, printShort: bool = False):
    #     for idx in range(6):
    #         for i, card in enumerate(self.hand):
    #             if printShort and i < len(self.hand)-1:
    #                 image = card.shortImage[idx]    if self.knownCards[i] else card.cardBack[idx]
    #                 print(image, end="")
    #             else:
    #                 image = card.image[idx] if self.knownCards[i] else card.cardBack[idx]
    #                 print(image, end="")
    #         print()

    def clearHand(self):
        self.hand = []
        self.knownCards = []