import os
import random
<<<<<<< HEAD
from cardgames.Card import Card
=======
from cardgames.Card_Compare import Card
>>>>>>> db21b8c5a013bc397b4233adf9963264716c5db1

cardImages = []
values = list(range(1,14))
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

def find_root_dir():
    cwd = os.getcwd()
    while 'src' not in os.listdir():
        os.chdir('..')
        cwd = os.path.join( cwd, '..')
    return cwd

class Deck:
    def __init__(self):
        root_dir = os.path.join( find_root_dir(), 'src')
        cards_file = os.path.join(root_dir, 'cardgames', 'playing_cards.txt')
        with open(cards_file, "r") as cards:
            cardBack = []
            for _ in range(6):
                line = cards.readline()
                cardBack.append(line.replace("\n",""))
            card = []
            level = 0
            for line in cards.readlines():
                if len(line) == 1:
                    cardImages.append(card)
                    level = 0
                    card = []
                    continue
                card.append(line.replace("\n",""))
                level += 1
            cardImages.append(card)
        
        deck = []
        index = 0
        for suit in suits:
            for value in values:
                deck.append(Card(suit, value, cardImages[index], cardBack))
                index += 1
        
        self.cards = deck
        self.size = len(deck)
        self.cardBack = cardBack
        self.discarded = []

    def reset(self):
        self.cards += self.discarded
        self.discarded = []
        self.size = len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def getCard(self):
        card = self.cards.pop()
        self.size -= 1
        self.discarded.append(card)
        return card