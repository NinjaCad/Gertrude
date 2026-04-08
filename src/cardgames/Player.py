from cardgames.Card import Card

class Player:
    def __init__(self, name, angle=0):      # player angle defaults to 0 if not passed in
        self.name = name
        self.angle = angle
        self.hand = []
        self.known_cards = []
        self.can_play = True  # flag to track if player can play cards

    # method to return the name of the player to keep the original object protected
    def get_name(self):
        return self.name

    # method to change the name of the player 
    def set_name(self, name: str):
        self.name = name

    # method to return the hand of the player to keep the original object protected
    def get_hand(self):
        return self.hand[:]

    def get_angle(self):
        return self.angle

    def set_angle(self, angle: float):
        self.angle = angle

    # changed addCard function to default the isKnown attrib to False, but still retain
    # some functionality if an explicit call to isKnown = True is needed for some reason.
    def add_card(self, card: Card, is_known: bool = False) -> None:
        self.hand.append(card)
        self.known_cards.append(is_known)

    def set_hand(self, cards: "list[Card]", is_known: bool = False) -> None:
        self.hand = cards

    def clear_hand(self) -> None:
        self.hand = []
        self.known_cards = []

    def pop_card(self):
        """
        Removes the last card from the player hand and 
        returns the card object.
        """
        if not self.hand:
            return None
        played_card = self.hand.pop()
        if self.known_cards:
            self.known_cards.pop()
        return played_card

def card_counter():
    ranks = [
        "Ace", "2", "3", "4", "5", "6", "7", 
        "8", "9", "10", "Jack", "Queen", "King"
    ]
    print("--- Global Card Counter ---")
    print("Press [ENTER] to see the next card value.")
    print("Press [Ctrl+C] to exit.\n")
    for rank in ranks:
        input(f"Next value: {rank}")