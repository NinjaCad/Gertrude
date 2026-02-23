from cardgames.Card import Card
from cardgames.Deck import Deck
from cardgames.Player import Player

class Dealer:
    def __init__(self, deck: Deck):
        self.deck = deck
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

    def dealCards(self, players: "list[Player]"):
        for cardNum in range(len(self.deck.cards)):
            players[cardNum % len(players)].addCard(self.deck.getCard())
        return True

    def resetDeck(self):
        self.deck.reset()
        self.deck.shuffle()