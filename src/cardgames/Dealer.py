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

    def dealCards(self, numCards: int, players: "list[Player]"):
        """Deal `numCards` cards round-robin to each player.
        If there aren't enough cards return False.
        By convention a player named 'GERTRUDE' receives their second card face-down
        (known=False)."""
        if numCards * len(players) > self.deck.size:
            return False

        for round_num in range(numCards):
            for player in players:
                # Dealer (GERTRUDE) hides their second card
                isKnown = True
                try:
                    name = getattr(player, "name", "")
                    if isinstance(name, str) and name.upper() == "GERTRUDE" and round_num == 1:
                        isKnown = False
                except Exception:
                    pass

                card = self.deck.getCard()
                player.addCard(card, isKnown)
        return True

    def resetDeck(self):
        self.deck.reset()
        self.deck.shuffle()


