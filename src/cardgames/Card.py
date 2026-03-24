class Card:
    def __init__(self, suit, value, image, card_back):
        self.card_back = card_back
        self.suit = suit
        self.value = value
        self.image = image
        self.short_image = []
        if self.image:
            for line in self.image:
                self.short_image.append(line[:4])

    def __str__(self, short: bool = False):
        return '\n'.join(self.short_image if short else self.image)

    def __eq__(self, other):
        if not type(other) == Card:
            return False
        return self.suit == other.suit and \
            self.value == other.value