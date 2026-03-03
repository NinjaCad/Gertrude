from cardgames.Card import Card
from cardgames.Deck import Deck
from cardgames.Player import Player

import random

class Dealer:
    def __init__(self, deck: Deck):
        self.deck = deck
        self.resetDeck()

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

    def resetDeck(self):
        self.deck.reset()
        # Shuffle the deck multiple times to ensure randomness
        for _ in range(7):
            self.deck.shuffle()
        # Cut the deck multiple times to further randomize the order
        for _ in range(3):
            cut = random.randint(0, self.deck.size)
            self.deck.cards = self.deck.cards[cut:] + self.deck.cards[:cut]
        