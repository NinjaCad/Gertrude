from .Card_Compare import Card
from .Deck import Deck
from .Player import Player

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

    def dealCards(self, numCards: int, players: "list[Player]"):
        if numCards * len(players) > self.deck.size:
            return False
        for player in players:
            for _ in range(numCards):
                player.addCard(self.deck.getCard())
        return True


    def resetDeck(self):
        self.deck.reset()
        self.deck.shuffle()

    def redraw_three_card_options(self, player: Player):
        # Allows a playeret to spend a token to draw 3 more cards.
        if self.deck.size < 3:
            self.resetDeck()
            if self.deck.size < 3:
                return False
        if not player.consume_redraw_token():
            return False
        player.clearHand()
        for _ in range(3):
            player.addCard(self.deck.getCard())
        return True