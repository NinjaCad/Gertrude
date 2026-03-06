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

    # GERT-33 dealCards()
    # inputs: players (list of player objects)
    # outputs: none
    # goals: a) given the list of players, give every player 2 cards
    #        b) for gertrude, make sure to give player aspect the cards. one of gertrude's cards is hidden
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


