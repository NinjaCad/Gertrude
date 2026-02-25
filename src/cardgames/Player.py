from cardgames.Card import Card

class Player:
    def __init__(self, name, player_id=None):
        self.id = player_id
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

    def checkForFourOfAKind(self):
        counts_list = (("Aces", 0), ("Twos", 0), ("Threes", 0), ("Fours", 0), ("Fives", 0), ("Sixes", 0), ("Sevens", 0), ("Eights", 0), ("Nines", 0), ("Tens", 0), ("Jacks", 0), ("Queens", 0), ("Kings", 0))
        isFourOfAKind = []
        numberOfFourOfAKindsInHand = 0
        for card in self.hand:
            index = card.value
            (key, value) = counts_list[index-1]
            value += 1
        for  i in range(1,14):
            (key, value) = counts_list[i-1]
            if value == 4:
                isFourOfAKind.append(key)
                numberOfFourOfAKindsInHand += 1
        if isFourOfAKind == []:
            return False
        else:
            return isFourOfAKind, numberOfFourOfAKindsInHand


    def clearHand(self):
        self.hand = []
        self.knownCards = []
