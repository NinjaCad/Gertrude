from cardgames.Card import Card

class Player:
    def __init__(self, name, angle=0):      #player angle defaults to 0 if not passed in
        self.name = name
        self.angle = angle
        self.hand = []
        self.known_cards = []

    #method to return the name of the player to keep the original object protected
    def get_name(self):
        return self.name

    #method to change the name of the player 
    def set_name(self, name):
        self.name = name

    #method to return the hand of the player to keep the original object protected
    def get_hand(self):
        return self.hand[:]

    # changed addCard function to default the isKnown attrib to False, but still retain
    # some functionality if an explicit call to isKnown = True is needed for some reason.
    def add_card(self, card: Card, is_known: bool = False) -> None:
        self.hand.append(card)
        self.known_cards.append(is_known)

    def set_hand(self, cards: "list[Card]", is_known: bool = False) -> None:
        self.hand = cards
        # remove the following line to leave all cards in hand at their default of "isKnown = False" 
        #self.knownCards = [isKnown for _ in self.hand]

    # Removed the showHand function because there's no need for it in our game.
    # def showHand(self, printShort: bool = False):
    #     for idx in range(6):
    #         for i, card in enumerate(self.hand):
    #             if printShort and i < len(self.hand)-1:
    #                 image = card.shortImage[idx]    if self.knownCards[i] else card.cardBack[idx]
    #                 print(image, end="")
    #             else:
    #                 image = card.image[idx] if self.knownCards[i] else card.cardBack[idx]
    #                 print(image, end="")
    #         print()

    def clear_hand(self) -> None:
        self.hand = []
        self.known_cards = []