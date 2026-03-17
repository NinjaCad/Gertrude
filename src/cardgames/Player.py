from cardgames.Card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.knownCards = []
        self.books = 0

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
        if len(self.hand) >= 4:
            countsDict = {"Aces": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0, "Sevens": 0, "Eights": 0, "Nines": 0, "Tens": 0, "Jacks": 0, "Queens": 0, "Kings": 0}
            isFourOfAKind = []
            numberOfFourOfAKindsInHand = 0
            valueMap = {1: "Aces", 2: "Twos", 3: "Threes", 4: "Fours", 5: "Fives", 6: "Sixes", 7: "Sevens", 8: "Eights", 9: "Nines", 10: "Tens", 11: "Jacks", 12: "Queens", 13: "Kings"}
            for card in self.hand:
                value = card.value
                key = valueMap.get(value, "")
                countsDict[key] += 1
            for (key, value) in countsDict.items():
                if value == 4:
                    isFourOfAKind.append(key)
                    numberOfFourOfAKindsInHand += 1
            return isFourOfAKind
        else:
            return []

    def bookHandling(self): #adds player books count (score increase) and removes the four of a kind cards from play
            valueMap = {'Aces': 1, 'Twos': 2, 'Threes': 3, 'Fours': 4, 'Fives': 5, 'Sixes': 6, 'Sevens': 7, 'Eights': 8, 'Nines': 9, 'Tens': 10, 'Jacks': 11, 'Queens': 12, 'Kings': 13}
            listOfBooks = self.checkForFourOfAKind()
            self.books += len(listOfBooks)
            for book in listOfBooks:
                bookValue = valueMap.get(book, 0)
                remainingHand = []
                remainingKnown = []
                for i, card in enumerate(self.hand):
                    if card.value != bookValue:
                        remainingHand.append(card)
                        remainingKnown.append(self.knownCards[i])
                self.hand = remainingHand
                self.knownCards = remainingKnown    

    def clearHand(self):
        self.hand = []
        self.knownCards = []