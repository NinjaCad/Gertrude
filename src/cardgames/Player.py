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

    def check_cards(self, hand):
        total_score = 0
        num_aces = 0

        for card_id in hand:
            rank_index = card_id % 13  # 0=Ace, 1=2, ..., 10=J, 11=Q, 12=K

            if rank_index == 0:        # It's an Ace
                val = 11
                num_aces += 1
            elif rank_index >= 10:     # It's a Face Card
                val = 10
            else:                      # It's 2 through 10
                val = rank_index + 1
            
            total_score += val

        # --- Blackjack Special Rule: Adjusting Aces ---
        # If the score is over 21 and we have an Ace (11), 
        # change it to a 1 (subtract 10) until we are safe.
        while total_score > 21 and num_aces > 0:
            total_score -= 10
            num_aces -= 1
        
        return total_score
    

    
