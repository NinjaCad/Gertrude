from cardgames.Card import Card
from cardgames.Card_Compare import *
import os

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.knownCards = []
<<<<<<< HEAD
        self.chosen_card = None
=======
        self.redraw_tokens = 0
        self.chosen_card = None
        self.chosen_card = Card("", 0, [], [])
>>>>>>> 96c1c706ed905127f82872d092a86f696cffd9fd

    def addCard(self, card: Card, isKnown: bool = True):
        self.hand.append(card)
        # We use isKnown so showHand knows whether to show the face or the back
        self.knownCards.append(isKnown)

    def setHand(self, cards: "list[Card]", isKnown: bool = True): # Changed default to True
        self.hand = cards
        self.knownCards = [isKnown for _ in self.hand]

    def showHand(self, printShort: bool = False):
        # Temporarily force knownCards to True if you want the player 
        # to ALWAYS see their own cards during their turn
        for idx in range(6):
            for i, card in enumerate(self.hand):
                # Logic: If knownCards[i] is True, show face. Else, show back.
                is_revealed = self.knownCards[i] 
                
                if printShort and i < len(self.hand)-1:
                    image = card.shortImage[idx] if is_revealed else card.cardBack[idx]
                    print(image, end="")
                else:
                    image = card.image[idx] if is_revealed else card.cardBack[idx]
                    print(image, end="")
            print()

    def hideHand(self):
        if self.hand:
            print("\x1b[2J\033[H")
            for idx in range(6):
                for card in self.hand:
                    print(card.cardBack[idx], end="")
                print()
<<<<<<< HEAD
            print(f"{self.name}'s hand is now hidden.")
=======
            
            print(f"\n{self.name}'s hand is now hidden.")
>>>>>>> 96c1c706ed905127f82872d092a86f696cffd9fd
        else:
            print(f"{self.name} has no cards to hide.")

    def clear_screen(self):
        # If the OS is Windows, run 'cls', otherwise run 'clear'
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def clearHand(self):
        self.hand = []
        self.knownCards = []
<<<<<<< HEAD
        # CRITICAL: Reset the chosen card so the next round starts fresh
        self.chosen_card = None
=======

    def add_redraw_token(self, tokens: int = 1):
        if tokens < 0:
            raise ValueError("Cannot add a negative number of redraw tokens.")
        self.redraw_tokens += tokens

    def record_round_win(self):
        self.add_redraw_token()

    def can_redraw(self) -> bool:
        return self.redraw_tokens > 0

    def consume_redraw_token(self) -> bool:
        if not self.can_redraw():
            return False
        self.redraw_tokens -= 1
        return True
>>>>>>> 96c1c706ed905127f82872d092a86f696cffd9fd
