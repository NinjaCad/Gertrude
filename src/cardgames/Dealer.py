from cardgames.Card import Card
from cardgames.Deck import Deck
from cardgames.Player import Player

class Dealer:
    def __init__(self, deck: Deck):
        self.deck = deck
        # They say it takes 7 shuffles to sufficiently randomize a deck of cards, so we'll do that here
        for _ in range(7):
            self.deck.shuffle()

    def printCards(self, cards: "list[Card]", showFront: bool, printShort: bool = True):
        for idx in range(6):
            for i, card in enumerate(cards):
                if printShort and i < len(cards)-1:
                    image = card.shortImage[idx] if showFront else card.cardBack[idx]
                    print(image, end="")
                else:
                    image = card.image[idx] if showFront else card.cardBack[idx]
                    print(image, end="")
            print()

    def dealCards(self, numCards: int, players: "list[Player]"):
        if numCards * len(players) > self.deck.size:
            return False
        for player in players:
            for _ in range(numCards):
                player.addCard(self.deck.getCard())
        return True

    def checkPair(self):
        counts = {}
        for card in self.deck.cards:
            if card.value in counts:
                return True
            else:
                counts[card.value] = 1
        return False

    def resetDeck(self):
        self.deck.reset()
        self.deck.shuffle()