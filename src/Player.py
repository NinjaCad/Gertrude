from Card import Card

class Player:
    def __init__(self, name, money: int = 0):
        self.name = name
        self.hand = []
        self.knownCards = []
        self.money = money

    def addMoney(self, amount: int):
        self.money += amount
        return self.money

    def makeBet(self, amount: int):
        if amount > self.money:
            print("%s does not have enough money to make this bet." % self.name)
            return self.money
        self.money -= amount
        return self.money

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