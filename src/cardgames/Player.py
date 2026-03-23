import random

from cardgames.Card import Card

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.knownCards = []
        # When True, contributes to main game loop asking the player if they want to stand/hit/etc
        # When False, that player will no longer be targeted in the game loop (when all players are False, round ends) 
        self.active = True

    def addCard(self, card: Card, isKnown: bool = True):
        self.hand.append(card)
        if isKnown:
            self.knownCards.append(True)
        else:
            self.knownCards.append(False)

    def setHand(self, cards: "list[Card]", isKnown: bool = False):
        self.hand = cards
        self.knownCards = [isKnown for _ in self.hand]
        self.knownCardsCount = 0

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
        
    # called to toggle active attribute of Player instances
    def stand(self):
        self.active = False if self.active == True else True
    
    # called when check_hand returns > 21, takes player out of turn rotation
    # assumption is that gameplay loop or check_cards() will call bust() when appropriate, so no additional logic is needed in this function
    def bust(self):
        self.active = False

    def check_cards(self):
        total_score = 0
        num_aces = 0

        for card_id in self.hand:
            rank_index = card_id.value  # 0=Ace, 1=2, ..., 10=J, 11=Q, 12=K

            if rank_index == 1:        # It's an Ace
                val = 11
                num_aces += 1
            elif rank_index >= 11:     # It's a Face Card
                val = 10
            else:                      # It's 2 through 10
                val = rank_index
            
            total_score += val

        # --- Blackjack Special Rule: Adjusting Aces ---
        # If the score is over 21 and we have an Ace (11), 
        # change it to a 1 (subtract 10) until we are safe.
        while total_score > 21 and num_aces > 0:
            total_score -= 10
            num_aces -= 1
        
        return total_score
    
    def show_partial_hand(self): # This method will need to be called every time a new card is added to the player's hand, and it will update the known cards accordingly.
        #For the dealer, we just need to call the function as many times as the dealer is supposed to reveal cards.
        for i in range(len(self.hand)):
            if self.knownCards[i]:
                print(self.hand[i].shortImage)
            else:
                print(self.hand[i].cardBack)
            
    def hit(self, dealer, isKnown: bool = True):
        # hit() now goes through dealer 
        deck = dealer.deck

        if deck.size <= 0:
            # we can change this to endgame() function when we come across that in future sprints
            raise RuntimeError("Deck is empty.")

        card = deck.getCard()
        self.addCard(card, isKnown)
        return card
    
        # Simple that prints the rules, the available commands, and the player's current hand and hand value
    def help(self, moves: list):
        # Basics of the game
        output = ("""
BLACKJACK (21) - HOW TO PLAY:

GOAL:
Beat the dealer by getting closer to 21 without going over.

CARD VALUES:
  - Number cards (2–10) = face value
  - Face cards (J, Q, K) = 10
  - Ace = 1 or 11

SETUP:
  - You and the dealer each get 2 cards
  - Your cards are face up
  - Dealer has 1 face up, 1 face down

PLAYER ACTIONS:
  - Hit: Take another card
  - Stand: Keep your hand
  - Double Down: Double bet, take 1 card only
  - Split: If you have 2 matching cards, split into 2 hands

BUST:
  - If your total goes over 21, you lose immediately

DEALER RULES:
  - Dealer reveals hidden card after your turn
  - Must hit until at least 17
  - Must stand on 17 or higher

WINNING:
  - Higher than dealer without busting = win
  - Dealer busts = win
  - Lower than dealer = lose
  - Tie = push (bet returned)

BLACKJACK:
  - Ace + 10-value card
  - Best possible hand
  - Pays extra (usually 3:2)

TIPS:
  - Hit if under 12
  - Stand on 17+
  - Play aggressive if dealer has 7 or higher
  - Be cautious if dealer has 4–6
""")

        # Print all the commands, their alternate name(s), and if they they can use it
        output += "\nCOMMANDS CURRENTLY AVAILABLE: "
        for name in moves:
            output += f"{name}, "

        # Prints the total value of the player's hand
        output += f"\n\nCURRENT HAND VALUE: {self.check_cards()}"
        output += "\n"

        return output
    
    # Just some fun trash talk lines that gertrude when the player busts
    def trashTalk(self):
        lines = [
            "Gertrude clicks her tongue: 'Over 21? That’s not bravery—that’s bad math.'",
            "Gertrude nods at your cards: 'Ah yes, the classic strategy: ignore the number 21.'",
            "Gertrude sighs: 'If you wanted to bust, you could’ve just said so.'",
            "Gertrude leans in: 'You were so close… to making a smarter decision.'",
            "Gertrude grins: 'You hit like 21 is just a suggestion.'",
            "Gertrude laughs: 'Don’t worry—lots of people panic-hit. Not *winners*, but people.'",
            "Gertrude smirks: 'Busted. The house appreciates your generous donation.'",
            "Gertrude shrugs: 'I’ve seen better decisions at a roulette table.'",
            "Gertrude politely: 'Next time, try stopping before your hand catches fire.'",
            "Gertrude laughs softly: 'And *that* is why we don’t get greedy.'",
            "Gertrude tilts her head: 'You know “hit” isn’t a personality trait, right?'",
            "Gertrude adjusts her sleeves: 'I’ll mark that down as: “Player vs. Basic Arithmetic.”'"
        ]
    
        return "\n" + random.choice(lines) + "\n"