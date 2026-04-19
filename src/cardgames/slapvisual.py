import random
import time
from PIL import Image
suit_icons = {'Hearts': '❤️', 'Diamonds': '♦️', 'Clubs': '♣️', 'Spades': '♠️'}
class HeartAttackGame:
    def __init__(self):
        self.count_sequence = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.current_count_index = 0
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = self.count_sequence.copy()
        self.pile = []
    def next_turn(self):
        shown_rank = self.count_sequence[self.current_count_index]
        actual_rank = random.choice(self.ranks)
        actual_suit = random.choice(self.suits)
        print(f"\n--- Player says: \"{shown_rank}!\" ---")
        print(f"--- [ Card revealed: {actual_rank} of {suit_icons[actual_suit]} ] ---")
        if shown_rank == actual_rank:
            print("\n🚨 HEART ATTACK! 🚨")
            self.trigger_slap()
        else:
            print("(No match. Keep counting...)")
        self.current_count_index = (self.current_count_index + 1) % len(self.count_sequence)
    def trigger_slap(self):
        input("QUICK! Press ENTER to slap the pile! ")
        print("SLAP")
        try:
            img = Image.open('point.png')
            img.show()
        except FileNotFoundError:
            print("\n[Visual: Red Dot Slap Registered]")
game = HeartAttackGame()
for _ in range(10):
    game.next_turn()
    time.sleep(1)import random
import time
from PIL import Image
suit_icons = {'Hearts': '❤️', 'Diamonds': '♦️', 'Clubs': '♣️', 'Spades': '♠️'}
class HeartAttackGame:
    def __init__(self):
        self.count_sequence = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.current_count_index = 0
        self.suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = self.count_sequence.copy()
        self.pile = []
    def next_turn(self):
        shown_rank = self.count_sequence[self.current_count_index]
        actual_rank = random.choice(self.ranks)
        actual_suit = random.choice(self.suits)
        print(f"\n--- Player says: \"{shown_rank}!\" ---")
        print(f"--- [ Card revealed: {actual_rank} of {suit_icons[actual_suit]} ] ---")
        if shown_rank == actual_rank:
            print("\n🚨 HEART ATTACK! 🚨")
            self.trigger_slap()
        else:
            print("(No match. Keep counting...)")
        self.current_count_index = (self.current_count_index + 1) % len(self.count_sequence)
    def trigger_slap(self):
        input("QUICK! Press ENTER to slap the pile! ")
        print("SLAP")
        try:
            img = Image.open('point.png')
            img.show()
        except FileNotFoundError:
            print("\n[Visual: Red Dot Slap Registered]")
game = HeartAttackGame()
for _ in range(10):
    game.next_turn()
    time.sleep(1) 