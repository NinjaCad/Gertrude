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

    def get_suit_rank(self):
        return Card.SUIT_RANKINGS.get(self.suit, 0)


#  Standalone comparison function
def compare_cards(card1, card2):
    if not isinstance(card1, Card) or not isinstance(card2, Card):
        raise TypeError("Both arguments must be Card objects")

    #  First compare values
    if card1.value > card2.value:
        return 1
    elif card1.value < card2.value:
        return -1

    #  If values are equal, compare suits
    suit1 = card1.get_suit_rank()
    suit2 = card2.get_suit_rank()

    if suit1 > suit2:
        return 1
    elif suit1 < suit2:
        return -1

    # 🔹 If both value AND suit are equal
    return 0
    return 0