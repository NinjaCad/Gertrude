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
    
    def removeCard(self, card: Card):
        self.hand.remove(card)
        #Not sure if we are using known cards at the moment, can add later.

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
            counts_dict = {"Aces": 0, "Twos": 0, "Threes": 0, "Fours": 0, "Fives": 0, "Sixes": 0, "Sevens": 0, "Eights": 0, "Nines": 0, "Tens": 0, "Jacks": 0, "Queens": 0, "Kings": 0}
            isFourOfAKind = []
            numberOfFourOfAKindsInHand = 0
            value_map = {1: "Aces", 2: "Twos", 3: "Threes", 4: "Fours", 5: "Fives", 6: "Sixes", 7: "Sevens", 8: "Eights", 9: "Nines", 10: "Tens", 11: "Jacks", 12: "Queens", 13: "Kings"}
            for card in self.hand:
                value = card.value
                key = value_map.get(value, "")
                counts_dict[key] += 1
            for (key, value) in counts_dict.items():
                if value == 4:
                    isFourOfAKind.append(key)
                    numberOfFourOfAKindsInHand += 1
            return isFourOfAKind
        else:
            return []

    def bookHandling(self): #Josiah requested we have this function so that we have a basis for when anyone tries to add the other book functions
        self.checkForFourOfAKind()

    def clearHand(self):
        self.hand = []
        self.knownCards = []