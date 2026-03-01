class Card:
    def __init__(self, suit, value, image, cardBack):
        self.cardBack = cardBack
        self.suit = suit
        self.value = value
        self.image = image
        self.shortImage = []
        if self.image:
            for line in self.image:
                self.shortImage.append(line[:4])

    def __str__(self):
        face_names = {1: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
        card_name = face_names.get(self.value, self.value)

        display_text = f"--- {card_name} of {self.suit} ---\n"

        for line in self.image:
            display_text += line + "\n"

        return display_text

    def __eq__(self, other):
        if not type(other) == Card:
            return False
        return self.suit == other.suit and self.value == other.value