from cardgames.Card_Compare import *

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.knownCards = []
        # Keeping the most common initialization
        self.chosen_card = None

    def addCard(self, card: Card, isKnown: bool = True):
        self.hand.append(card)
        if isKnown:
            self.knownCards.append(True)
        else:
            self.knownCards.append(False)

    def setHand(self, cards: "list[Card]", isKnown: bool = False):
        self.hand = cards
        self.knownCards = [isKnown for _ in self.hand]

    def showHand(self, printShort: bool = False):
        for idx in range(6):
            for i, card in enumerate(self.hand):
                if printShort and i < len(self.hand)-1:
                    image = card.shortImage[idx] if self.knownCards[i] else card.cardBack[idx]
                    print(image, end="")
                else:
                    image = card.image[idx] if self.knownCards[i] else card.cardBack[idx]
                    print(image, end="")
            print()

    def hideHand(self):
        if self.hand:
            # Clears the terminal
            print("\x1b[2J\033[H")

            # Print the card backs of all cards in the player's hand
            for idx in range(6):
                for card in self.hand:
                    print(card.cardBack[idx], end="")
                print()
            
            print(f"{self.name}'s hand is now hidden.")
        else:
            print(f"{self.name} has no cards to hide.")

    def clearHand(self):
        self.hand = []
        self.knownCards = []