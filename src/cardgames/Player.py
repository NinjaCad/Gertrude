from cardgames.Card_Compare import *

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.knownCards = []
        self.chosen_card = None

    def addCard(self, card: Card, isKnown: bool = True):
        self.hand.append(card)
        # We use isKnown so showHand knows whether to show the face or the back
        self.knownCards.append(isKnown)

    def setHand(self, cards: "list[Card]", isKnown: bool = True): # Changed default to True
        self.hand = cards
        self.knownCards = [isKnown for _ in self.hand]

    def showHand(self, printShort: bool = False):
        # Temporarily force knownCards to True if you want the player 
        # to ALWAYS see their own cards during their turn
        for idx in range(6):
            for i, card in enumerate(self.hand):
                # Logic: If knownCards[i] is True, show face. Else, show back.
                is_revealed = self.knownCards[i] 
                
                if printShort and i < len(self.hand)-1:
                    image = card.shortImage[idx] if is_revealed else card.cardBack[idx]
                    print(image, end="")
                else:
                    image = card.image[idx] if is_revealed else card.cardBack[idx]
                    print(image, end="")
            print()

    def hideHand(self):
        if self.hand:
            print("\x1b[2J\033[H")
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
        # CRITICAL: Reset the chosen card so the next round starts fresh
        self.chosen_card = None