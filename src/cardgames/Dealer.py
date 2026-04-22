<<<<<<< HEAD
from cardgames.Card import Card
=======
>>>>>>> origin/dev_backrow_buggers
from cardgames.Card_Compare import Card
from cardgames.Deck import Deck
from cardgames.Player import Player

class Dealer:
    def __init__(self, deck: Deck):
        self.deck = deck
        self.deck.shuffle()

    def printCards(self, cards: "list[Card]", showFront: bool, printShort: bool = True):
        for idx in range(6):
            for i, card in enumerate(cards):
                if printShort and i < len(cards)-1:
                    image = card.shortImage[idx] if showFront else card.cardBack[idx]
                    print(image, end="")
                else:
                    image = card.image[idx] if showFront else card.cardBack[idx]
                    print(image, end="")
            print()

    # was def dealCards(self, numCards_or_players, players: "list[Player]" = None):
    def dealCards(self, numCards_or_players, players: "list[Player] | None" = None):
        # Backward compatibility:
        # - dealCards(3, players)
        # - dealCards(players)  -> defaults to 3 cards/player
        if players is None:
            players = numCards_or_players
            numCards = 3
        else:
            numCards = numCards_or_players
        
        # I added this to make sure the list isn't empty -- Tyson
        if not players or not isinstance(players, list):
            return False

        if numCards * len(players) > self.deck.size:
            return False
        for player in players:
            for _ in range(numCards):
                player.addCard(self.deck.getCard())
        return True

    def resetDeck(self):
        self.deck.reset()
        self.deck.shuffle()

    def redraw_three_card_options(self, player: Player):
        # Allows a playeret to spend a token to draw 3 more cards.
        if self.deck.size < 3:
            self.resetDeck()
            if self.deck.size < 3:
                return False
        if not player.consume_redraw_token():
            return False
        player.clearHand()
        for _ in range(3):
            player.addCard(self.deck.getCard())
        return True