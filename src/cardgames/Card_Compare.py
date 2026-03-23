class Card:
    # Suit rankings: higher number = better
    SUIT_RANKINGS = {
        "Clubs": 4,
        "Diamonds": 3,
        "Hearts": 2,
        "Spades": 1
    }

    def __init__(self, suit, value, image, cardBack):
        self.cardBack = cardBack
        self.suit = suit
        self.value = value
        self.image = image
        self.shortImage = []
        if self.image:
            for line in self.image:
                self.shortImage.append(line[:4])

    def __str__(self, short: bool = False):
        return '\n'.join(self.shortImage if short else self.image)

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.suit == other.suit and self.value == other.value

    def _get_suit_rank(self):
        return Card.SUIT_RANKINGS.get(self.suit, 0)

    def compare(self, other):
        if not isinstance(other, Card):
            raise TypeError("Can only compare one Card with anotherCard")

        # compare values
        if self.value > other.value:
            return 1
        elif self.value < other.value:
            return -1

        # If values equal, compare suits
        suit1 = self._get_suit_rank()
        suit2 = other._get_suit_rank()

        if suit1 > suit2:
            return 1
        elif suit1 < suit2:
            return -1

        return 0