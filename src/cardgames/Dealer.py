from cardgames.Card import Card
from cardgames.Deck import Deck

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

    def dealCards(self, numCards: int, players):
        """Deal `numCards` cards round-robin to each player.
        If there aren't enough cards return False.
        'GERTRUDE' receives their second card face-down
        (known=False)."""
        if numCards * len(players) > self.deck.size:
            return False

        for deal_pass in range(numCards):
            for player in players:
                # 1. Default to True (most cards are face-up)
                isKnown = True
                
                # We check isinstance to prevent AttributeErrors without needing try/except.
                name = getattr(player, "name", "")
                
                if isinstance(name, str) and name.upper() == "GERTRUDE":
                    if deal_pass == 1:
                        isKnown = False  # The dealer's second card is hidden
                
                card = self.deck.getCard()
                player.addCard(card, isKnown)
        return True
    
    def resetDeck(self):
        self.deck.reset()
        self.deck.shuffle()