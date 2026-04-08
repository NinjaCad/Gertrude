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
                
#     def __init__(self, suit_inp, value):
#         suits = {
#     "S": {"symbol": "♠", "name": "Spades"},
#     "H": {"symbol": "♥", "name": "Hearts"},
#     "D": {"symbol": "♦", "name": "Diamonds"},
#     "C": {"symbol": "♣", "name": "Clubs"}
# }
#         if suit_inp == 'S':
#                 self.suit = suits["S"]["symbol"]

#         elif suit_inp == 'H':
#             self.suit = suits["H"]["symbol"]

#         elif suit_inp == 'D':
#             self.suit = suits["D"]["symbol"]

#         elif suit_inp == 'C':
#             self.suit = suits["C"]["symbol"]
        
#         values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
#         self.value = value
#         self.image = f"""\
# +---------+
# | {self.value:<2}    {self.suit} |
# |         |
# |    {self.suit}    |
# |         |
# | {self.suit}    {self.value:>2} |
# +---------+
# """
#         self.cardBack = """\
# +---------+
# |░░░░░░░░░|
# |░  ◇◇◇  ░|
# |░  ◇◇◇  ░|
# |░  ◇◇◇  ░|
# |░░░░░░░░░|
# +---------+
# """
#         self.shortImage = [f'{self.suit}{self.value}']

#         return self.shortImage, self.image

    def __str__(self, short: bool = False):
        return '\n'.join(self.shortImage if short else self.image)

    def __eq__(self, other):
        if not type(other) == Card:
            return False
        return self.suit == other.suit and \
            self.value == other.value