from cardgames.Card_Compare import *
import os


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.knownCards = []
        self.chosen_card = Card("", 0, [], [])

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
                    image = card.image if self.knownCards[i] else card.cardBack[idx]
                    print(image, end="")
            print()

    def hideHand(self):
        if self.hand:
            hidden = self.name

            #Clears the terminal
            print("\x1b[2J\033[H")

            #Print the card backs of all cards in the player's hand
            for idx in range(6):
                for card in self.hand:
                    print(card.cardBack[idx], end="")
                print()
            
            print(f"\n{self.name}'s hand is now hidden.")
        else:
            print(f"{self.name} has no cards to hide.")

    def clear_screen(self):
        # If the OS is Windows, run 'cls', otherwise run 'clear'
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def clearHand(self):
        self.hand = []
        self.knownCards = []