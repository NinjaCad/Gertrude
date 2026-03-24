from cardgames.Card import Card
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.knownCards = []
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
                    image = card.shortImage[idx]    if self.knownCards[i] else card.cardBack[idx]
                    print(image, end="")
                else:
                    image = card.image[idx] if self.knownCards[i] else card.cardBack[idx]
                    print(image, end="")
            print()
    def clearHand(self):
        self.hand = []
        self.knownCards = []
    def pop_card(self):
        """
        Removes the last card from the player hand and 
        returns the card object.
        """
        if not self.hand:
            return None
        played_card = self.hand.pop()
        if self.knownCards:
            self.knownCards.pop()
        return played_card
def card_counter():
    ranks = [
        "Ace", "2", "3", "4", "5", "6", "7", 
        "8", "9", "10", "Jack", "Queen", "King"
    ]
    print("--- Global Card Counter ---")
    print("Press [ENTER] to see the next card value.")
    print("Press [Ctrl+C] to exit.\n")
    for rank in ranks:
        input(f"Next value: {rank}")
if __name__ == "__main__":