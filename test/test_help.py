from testing_base import * 

def test_help():
    game = Games()

    #TEST CASE #1:
    moves = {
            "hit": {
                "enabled": True,
                "aliases": {"h"},
            },
            "stand": {
                "enabled": True,
                "aliases": {"s"},
            }
            }
    test1 = Player("test1")
    game.help(test1, moves)
    #EXCEPTED OUTPUT:
        # BLACKJACK (21) - HOW TO PLAY:

        # GOAL:
        # Beat the dealer by getting closer to 21 without going over.

        # CARD VALUES:
        #   - Number cards (2–10) = face value
        #   - Face cards (J, Q, K) = 10
        #   - Ace = 1 or 11

        # SETUP:
        #   - You and the dealer each get 2 cards
        #   - Your cards are face up
        #   - Dealer has 1 face up, 1 face down

        # PLAYER ACTIONS:
        #   - Hit: Take another card
        #   - Stand: Keep your hand
        #   - Double Down: Double bet, take 1 card only
        #   - Split: If you have 2 matching cards, split into 2 hands

        # BUST:
        #   - If your total goes over 21, you lose immediately

        # DEALER RULES:
        #   - Dealer reveals hidden card after your turn
        #   - Must hit until at least 17
        #   - Must stand on 17 or higher

        # WINNING:
        #   - Higher than dealer without busting = win
        #   - Dealer busts = win
        #   - Lower than dealer = lose
        #   - Tie = push (bet returned)

        # BLACKJACK:
        #   - Ace + 10-value card
        #   - Best possible hand
        #   - Pays extra (usually 3:2)

        # TIPS:
        #   - Hit if under 12
        #   - Stand on 17+
        #   - Play aggressive if dealer has 7 or higher
        #   - Be cautious if dealer has 4–6
                
        # COMMANDS CURRENTLY AVAILABLE:
        #   - hit (h) [enabled]
        #   - stand (s) [enabled]

        # CURRENT HAND:







        # CURRENT HAND VALUE: 0
    
    # TEST CASE #2:
        #deck = Deck()
        #test2.hand.append(deck.getCard())
        #test2.hand.append(deck.getCard())
    moves = {
            "split": {
                "enabled": False,
                "aliases": {"sp"},
            },
            "double down": {
                "enabled": False,
                "aliases": {"dd"},
            }
            }
    test2 = Player("test2")
    test2.hand.append(Card("Spades", 0, ["  ___  ",
                                            " |A  | ",
                                            " | /\\| ",
                                            " | \\/| ",
                                            " |  A| ",
                                            "  ---  "],
                                            [" ___  ",
                                            "|A  | ",
                                            "| /\\| ",
                                            "| \\/| ",
                                            "|  A| ",
                                            " ---  "]))
    test2.hand.append(Card("Spades", 10, ["  ___  ",
                                            " |10 | ",
                                            " | /\\| ",
                                            " | \\/| ",
                                            " | 10| ",
                                            "  ---  "],
                                            [" ___  ",
                                            "|10 | ",
                                            "| /\\| ",
                                            "| \\/| ",
                                            "| 10| ",
                                            " ---  "]))
    test2.knownCards = [True for _ in test2.hand]
    game.help(test2, moves)
    #EXCEPTED OUTPUT:
        # BLACKJACK (21) - HOW TO PLAY:

        # GOAL:
        # Beat the dealer by getting closer to 21 without going over.

        # CARD VALUES:
        #   - Number cards (2–10) = face value
        #   - Face cards (J, Q, K) = 10
        #   - Ace = 1 or 11

        # SETUP:
        #   - You and the dealer each get 2 cards
        #   - Your cards are face up
        #   - Dealer has 1 face up, 1 face down

        # PLAYER ACTIONS:
        #   - Hit: Take another card
        #   - Stand: Keep your hand
        #   - Double Down: Double bet, take 1 card only
        #   - Split: If you have 2 matching cards, split into 2 hands

        # BUST:
        #   - If your total goes over 21, you lose immediately

        # DEALER RULES:
        #   - Dealer reveals hidden card after your turn
        #   - Must hit until at least 17
        #   - Must stand on 17 or higher

        # WINNING:
        #   - Higher than dealer without busting = win
        #   - Dealer busts = win
        #   - Lower than dealer = lose
        #   - Tie = push (bet returned)

        # BLACKJACK:
        #   - Ace + 10-value card
        #   - Best possible hand
        #   - Pays extra (usually 3:2)

        # TIPS:
        #   - Hit if under 12
        #   - Stand on 17+
        #   - Play aggressive if dealer has 7 or higher
        #   - Be cautious if dealer has 4–6
                
        # COMMANDS CURRENTLY AVAILABLE:
        #   - split (sp) [disabled]
        #   - double down (dd) [disabled]

        # CURRENT HAND:
        #   ___    ___  
        #  |A  |  |10 | 
        #  | /\|  | /\| 
        #  | \/|  | \/| 
        #  |  A|  | 10| 
        #   ---    ---  

        # CURRENT HAND VALUE: 21

if __name__ == "__main__":
    test_help()