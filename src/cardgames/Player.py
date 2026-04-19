from cardgames.Card_Compare import *
import os


class Player:
    def __init__(self, name, nickname=None, level="Beginner"):
        self.name = name
        self.nickname = nickname.strip() if isinstance(nickname, str) and nickname.strip() else name
        self.level = self._normalize_level(level)
        self.xp = 0
        self.hand = []
        self.knownCards = []
        self.redraw_tokens = 0
        self.chosen_card = None
        self.chosen_card = Card("", 0, [], [])

    def _normalize_level(self, level):
        if not isinstance(level, str):
            return "Beginner"
        cleaned = level.strip().title()
        if cleaned in ["Beginner", "Intermediate", "Advanced"]:
            return cleaned
        return "Beginner"

    def profile_display_name(self):
        if self.nickname and self.nickname != self.name:
            return f"{self.name} ({self.nickname})"
        return self.name

    def add_xp(self, amount: int = 1):
        if amount < 0:
            raise ValueError("XP amount cannot be negative.")
        self.xp += amount

    def get_xp(self) -> int:
        return self.xp

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
                    image = card.shortImage[idx] if self.knownCards[i] else card.cardBack[idx]
                    print(image, end="")
                else:
                    image = card.image if self.knownCards[i] else card.cardBack[idx]
                    print(image, end="")
            print()

    def hideHand(self):
        if self.hand:
            hidden = self.name

            #Clears the terminal
            print("\x1b[2J\033[H")

            #Print the card backs of all cards in the player's hand
            for idx in range(6):
                for card in self.hand:
                    print(card.cardBack[idx], end="")
                print()
            
            print(f"\n{self.name}'s hand is now hidden.")
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