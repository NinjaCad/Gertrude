from cardgames.Card import Card
from cardgames.Deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.knownCards = []
        self.numBooks = 0
        self.books = []
        self.isTurn = False

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

    def sortHand(self):
        paired = list(zip(self.hand, self.knownCards))
        paired.sort(key=lambda p: p[0].value)
        self.hand = [card for card, _ in paired]
        self.knownCards = [known for _, known in paired]

    def sortHandIntoValues(self):
        sorted_hand = sorted(self.hand, key=lambda card: card.value)
        return sorted_hand

    def groupHandByValues(self):
        value_map = {
        1: "As", 2: "2s", 3: "3s", 4: "4s", 5: "5s", 6: "6s", 7: "7s",
        8: "8s", 9: "9s", 10: "10s", 11: "Js", 12: "Qs", 13: "Ks"
        }

        sorted_hand = self.sortHandIntoValues()
        grouped_values = {}
        for card in sorted_hand:
            key = value_map.get(card.value, f"{card.value}s")
            if key not in grouped_values:
                grouped_values[key] = []
            grouped_values[key].append(card)
        return grouped_values

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
            self.books += listOfBooks
            self.numBooks += len(listOfBooks)
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
            if listOfBooks == []:
                return False
            else:
                return True

    def showBooks(self):
        valueMap = {"Aces": 1, "Twos": 2, "Threes": 3, "Fours": 4, "Fives": 5, "Sixes": 6, "Sevens": 7, "Eights": 8, "Nines": 9, "Tens": 10, "Jacks": 11, "Queens": 12, "Kings": 13}
        deck = Deck()
        printList = []
        # Looks through a deck to find needed cards
        for bookType in self.books:
            for card in deck.cards:
                try:
                    if card.value == valueMap[bookType]:
                        printList.append(card)
                except KeyError:
                    print("Error! Value in player.books is not correct!")
                    break

        # Prints books in groups
        for idx in range(6):
            for i, card in enumerate(printList):
                if (i + 1) % 4 in range(1, 4):
                    image = card.shortImage[idx]
                    print(image, end="")
                else:
                    image = card.image[idx]
                    print(image, end=" ")
            print()   

    def clearHand(self):
        self.hand = []
        self.knownCards = []

    def takeTurn(self, players, game):
        #This check catches recursion calls after the last book is made so that no mater what way leads to the 13th book being made, if it is then this function call ends so that the main game loop moves forward to the ending state (implemented in games.py while loop in main()).
        if game.dealer.checkFor13Books(players) == True:
            return
        else:
            ### Show books
            if self.numBooks != 0:
                print("\nYour books: ")
                self.showBooks()
            
            ### Testing if all opponents' hands are empty
            noCardsPlayers = []
            for player in players:
                if not player.isTurn and player.hand == []: # Skips the player whos turn it is, and takes players with empty hands
                    noCardsPlayers.append(player)
            
            ### If opponents' hands are empty and Deck is empty, skip
            if len(noCardsPlayers) == len(players) - 1 and len(game.deck.cards) == 0:
                print("\nThe deck and everyone elses' hands are empty! Nothing to do but skip...")
                return

        ### If opponents' hands are empty, draw
        if len(noCardsPlayers) == len(players) - 1 and len(game.deck.cards) != 0:
            print("\nEveryone elses' hands are empty! Nothing to do but draw...", '')
            self.hand.append(game.deck.getCard())
            self.knownCards.append(True)
            print("You picked up:")
            self.showHand()
            if self.bookHandling():
                print(r"""
██╗   ██╗ ██████╗ ██╗   ██╗██╗   ██╗███████╗    ███╗   ███╗ █████╗ ██████╗ ███████╗     █████╗     ██████╗  ██████╗  ██████╗ ██╗  ██╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║██║   ██║██╔════╝    ████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗    ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝██║
 ╚████╔╝ ██║   ██║██║   ██║██║   ██║█████╗      ██╔████╔██║███████║██║  ██║█████╗      ███████║    ██████╔╝██║   ██║██║   ██║█████╔╝ ██║
  ╚██╔╝  ██║   ██║██║   ██║╚██╗ ██╔╝██╔══╝      ██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██║    ██╔══██╗██║   ██║██║   ██║██╔═██╗ ╚═╝
   ██║   ╚██████╔╝╚██████╔╝ ╚████╔╝ ███████╗    ██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██║  ██║    ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗██╗
   ╚═╝    ╚═════╝  ╚═════╝   ╚═══╝  ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═╝  ╚═╝    ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝
                      """)
                self.showBooks()
                input("\nYou get to go again! Hit ENTER to continue...")
                self.takeTurn(players, game)
            return

            ### If hand is empty draw a card
        if len(self.hand) == 0: 
            print("\nYour hand is empty! ", '')
            self.hand.append(game.deck.getCard())
            self.knownCards.append(True)
            print("You picked up:")
            self.showHand()
            return

        ### Show hand
        #self.hand = self.sortHandIntoValues()
        #print("\nYour hand:")
        #self.showHand()

        ### Stealing cards
        stoleACard, requestedCard, pickedCard = game.card_thievery(players, self)
        if stoleACard:
            print(r""" 
██╗   ██╗ ██████╗ ██╗   ██╗    ███████╗████████╗ ██████╗ ██╗     ███████╗    ███████╗ ██████╗ ███╗   ███╗███████╗     ██████╗ █████╗ ██████╗ ██████╗ ███████╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║    ██╔════╝╚══██╔══╝██╔═══██╗██║     ██╔════╝    ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██║
 ╚████╔╝ ██║   ██║██║   ██║    ███████╗   ██║   ██║   ██║██║     █████╗      ███████╗██║   ██║██╔████╔██║█████╗      ██║     ███████║██████╔╝██║  ██║███████╗██║
  ╚██╔╝  ██║   ██║██║   ██║    ╚════██║   ██║   ██║   ██║██║     ██╔══╝      ╚════██║██║   ██║██║╚██╔╝██║██╔══╝      ██║     ██╔══██║██╔══██╗██║  ██║╚════██║╚═╝
   ██║   ╚██████╔╝╚██████╔╝    ███████║   ██║   ╚██████╔╝███████╗███████╗    ███████║╚██████╔╝██║ ╚═╝ ██║███████╗    ╚██████╗██║  ██║██║  ██║██████╔╝███████║██╗
   ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝   ╚═╝    ╚═════╝ ╚══════╝╚══════╝    ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝     ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝                                                                                                                                                    
      """)
            if self.bookHandling():
                print(r""" 
██╗   ██╗ ██████╗ ██╗   ██╗██╗   ██╗███████╗    ███╗   ███╗ █████╗ ██████╗ ███████╗     █████╗     ██████╗  ██████╗  ██████╗ ██╗  ██╗██╗
╚██╗ ██╔╝██╔═══██╗██║   ██║██║   ██║██╔════╝    ████╗ ████║██╔══██╗██╔══██╗██╔════╝    ██╔══██╗    ██╔══██╗██╔═══██╗██╔═══██╗██║ ██╔╝██║
 ╚████╔╝ ██║   ██║██║   ██║██║   ██║█████╗      ██╔████╔██║███████║██║  ██║█████╗      ███████║    ██████╔╝██║   ██║██║   ██║█████╔╝ ██║
  ╚██╔╝  ██║   ██║██║   ██║╚██╗ ██╔╝██╔══╝      ██║╚██╔╝██║██╔══██║██║  ██║██╔══╝      ██╔══██║    ██╔══██╗██║   ██║██║   ██║██╔═██╗ ╚═╝
   ██║   ╚██████╔╝╚██████╔╝ ╚████╔╝ ███████╗    ██║ ╚═╝ ██║██║  ██║██████╔╝███████╗    ██║  ██║    ██████╔╝╚██████╔╝╚██████╔╝██║  ██╗██╗
   ╚═╝    ╚═════╝  ╚═════╝   ╚═══╝  ╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝    ╚═╝  ╚═╝    ╚═════╝  ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝
                      """)
            if game.dealer.checkFor13Books(players) == True:
                return
            input("\nYou get to go again, press ENTER to continue...")
            self.takeTurn(players, game)
        else:
            if self.bookHandling(): # If picked up card makes a book
                print("\nLucky draw, you've made a book!")
                print("\nYour books: ")
                self.showBooks()
            if pickedCard != None:
                if requestedCard == pickedCard.value: # If the player picks up the card they asked another player for
                    print("\nYou picked up the same card you asked for!")
                    input("\nYou get to go again, press ENTER to continue...")
                    self.takeTurn(players, game)
                else:
                    if self.bookHandling(): # If picked up card makes a book
                        print("\nLucky draw, you've made a book!")
                        print("\nYour books: ")
                        self.showBooks()
                    if pickedCard != None:
                        if requestedCard == pickedCard.value: # If the player picks up the card they asked another player for
                            print("\nYou picked up the same card you asked for!")
                            input("\nYou get to go again, press ENTER to continue...")
                            self.takeTurn(players, game)
                        else:
                            input("\nEnd of your turn! Hit enter to continue...")
