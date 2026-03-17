from cardgames.Card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.knownCards = []

    def hide_card(self, index: int | None = None):
        """Hide a card in the player's hand by marking it as unknown.

        This uses the existing `knownCards` list where `False` means the card
        should be displayed with the card back.

        Args:
            index: Which card to hide (0-based). If None, hides the last card.

        Raises:
            IndexError: if the index is out of range or the hand is empty.
        """
        if not self.hand:
            raise IndexError("Cannot hide a card: hand is empty")

        if index is None:
            index = len(self.hand) - 1

        if index < 0 or index >= len(self.hand):
            raise IndexError(f"Card index out of range: {index}")

        # Ensure knownCards stays aligned with hand.
        if len(self.knownCards) != len(self.hand):
            self.knownCards = [True for _ in self.hand]

        self.knownCards[index] = False

    # Backwards-compatible alias (some sprints used camelCase naming).
    def hideCard(self, index: int | None = None):
        return self.hide_card(index)

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
                    image = card.shortImage[idx]    if self.knownCards[i] else card.cardBack[idx]
                    print(image, end="")
                else:
                    image = card.image[idx] if self.knownCards[i] else card.cardBack[idx]
                    print(image, end="")
            print()

    def clearHand(self):
        self.hand = []
        self.knownCards = []