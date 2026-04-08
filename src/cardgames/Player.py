import random

from cardgames.Card import Card
#from cardgames.Deck import Deck
#from cardgames.Dealer import Dealer

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.knownCards = []
        # When True, contributes to main game loop asking the player if they want to stand/hit/etc
        # When False, that player will no longer be targeted in the game loop (when all players are False, round ends) 
        self.active = True
        
        # GERT-18 initialize money and bet attributes for player
        self.money = 100
        self.bets = {"standard": 0, "insurance": 0, "pairs": 0, "21+3": 0}
        
        # GERT-15 for recording split() functionality
        self.split_hands_score = { }

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
    
    # GERT-16
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
        
    # stand()
    # inputs: none
    # outputs: none
    # goal: change self.active to false when player stands so they can no longer make moves
    def stand(self):
        self.active = False if self.active == True else True
    
    # bust()
    # inputs: none
    # outputs: none
    # goal: change self.active to false when player busts so they can no longer make moves
    
    # called when check_hand returns > 21, takes player out of turn rotation
    # assumption is that gameplay loop or check_cards() will call bust() when appropriate, so no additional logic is needed in this function
    def bust(self):
        # GERT-30 call trashtalk when player busts
        self.active = False


    #This function takes the card in a players hand and assigns in to its respective point value. 
    #Built into this function is ace logic (1 vs 11) and busting if the score goes over 21
    #Each players score is then returned 
    # check_cards()
    # inputs: none
    # outputs: score of hand (integer)
    # goal: determine the score of the player's hand
    # suggestions: a) hand parameter is not necessary, as player class can target self.hand. so use self.hand instead of hand
    #              b) GERT-37 before returning, check if the score is > 21 and bust if so
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
        if total_score > 21:
            self.bust()  # Player busts if score exceeds 21 even after adjusting Aces
            return total_score
        else:
            return total_score
        
    
    # show_partial_hand()
    # inputs: none
    # outputs: none
    # goal: print value of every known card and the back of every unkown card (GERT-16)
    # suggestions: none
    def show_partial_hand(self): # This method will need to be called every time a new card is added to the player's hand, and it will update the known cards accordingly.
        #For the dealer, we just need to call the function as many times as the dealer is supposed to reveal cards.
        for i in range(len(self.hand)):
            if self.knownCards[i]:
                print(self.hand[i].shortImage)
            else:
                print(self.hand[i].cardBack)
    
    # hit()
    # inputs: dealer (Dealer object), isKnown (boolean)
    # outputs: card (Card object)
    # goal: add a card from the game deck to the player hand
    # suggestions: none
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
    # GERT-30 trashtalk()
    # inputs: player (player object)
    # outputs: none
    # goals: have "gertrude" trashtalk player (incorporate player name in message so target is apparent >:) )
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
    # GERT-18 bet()
    # inputs: none
    # ouputs: none
    # goal: a) create new self.money and self.bet_money attributes
    #       b) set self.bet_money based on user input
    def bet(self, type):
        # GERT-30 call trashtalk when player makes a bet
        
        while True: # while loop guarantees valid input
            # Getting players money
            if (type == "pairs"):
                bet = input(f"{self.name}, you have ${self.money}. How much do you want to bet for perfect pairs? ")
            elif (type == "insurance"):
                bet = input(f"{self.name}, you previously bet ${self.bets['standard']}. You can bet up to half for insurance! How much would you like to bet? ") 
            else:
                bet = input(f"{self.name}, you have ${self.money}. How much do you want to bet? ")
            
            # guarantee that bet is an integer
            try:
                bet = int(bet)
            except ValueError:
                print("Please enter a valid integer amount.")
                continue
            
            # constraints
            if type == "standard" and bet < 5: # guarantee bet is 5 or more
                print("Bet amount must be at least $5. Please enter a valid amount.")
                continue
            if type == "insurance" and bet > self.bets["standard"] // 2:
                print(f"Insurance bet cannot be more than half of your original bet (${self.bets['standard']}). Please enter a valid amount")
                continue
            
            elif self.money - bet < -100: # guarantee player doesn't go more than $100 in debt
                print(f"You cannot go more than $100 in debt. Be responsible!")
                continue
            
            else: # if all checks are passed, set bet and break loop
                if (type == "pairs"):
                    self.bets["pairs"] = bet
                elif (type == "insurance"):
                    self.bets["insurance"] = bet
                else:
                    self.bets["standard"] = bet
                break
            
        return

    
    # GERT-18 resolve_bet()
    # inputs: win (dictionary where keys are the type of bet ("standard", "insurance", etc., and values are True or False based on whether or not bet was won)
    # example inputs: {"standard": True}
    #                 {"srandard": True, "insurance": False, "pairs": True}
    #                 {"insurance": True}
    # AKA, you can pass in all bets at once or one at a time depending on when and how we resolve the different bets. Order does not matter. Not every bet needs to be resolved at once.
    # outputs: none
    # goal: a) add or subtract bet attribute from money attribute based on whether or not player one
    def resolve_bet(self, bet_results):
        
        for bet in bet_results.keys():
            if bet_results[bet]:
                self.money += self.bets[bet]
            else:
                self.money -= self.bets[bet]
                
            self.bets[bet] = 0
            
        return
    
    # GERT-32 insurance()
    # inputs: none
    # outputs: none
    # goals: get the users bet and assign it to self.bets["insurance"]. make sure bet input is valid.
    def insurance(self, gert):
        if gert.hand[0].value == 1 and gert.hand[1].value >= 10: #Checking for Ace! 
            return True  
        else:
            return False  
    
    # GERT-40 perfectPairs()
    # inputs: none
    # outputs: pairType (string) based on whether or not there is a mixed pair, colored pair, or no pair
    # goals: check self.hand for mixed or colored pair
    def perfectPairs(self):
        if len(self.hand) == 2:
            if self.hand[0].value == self.hand[1].value:
                if self.hand[0].suit == self.hand[1].suit:
                    return "Colored Pair"
                else:
                    return "Mixed Pair"
        return False


    # GERT-15 split()
    # inputs: none
    # outputs: none (may change)
    # goals: create two subhands that can each play in any order, by splitting the current hand
    #        play each hand until completion (aka stand or bust)
    #        set self.active to false
    #        to avoid messing with round() or main() structure in Games.py, all split functionality
    #        will be completely handled here
    def split(self, dealer):
        
        hands = {"L": Player("L"), "R": Player("R")}
        hands["L"].addCard(self.hand[0], True)
        hands["R"].addCard(self.hand[1], True)
        
        hand = None
        while hands["L"].active or hands["R"].active: # mini game loop to complete split
            
            if hand:
                if hand == "L":
                    print(f"\n--- R's hand ---")
                    hands["R"].showHand()
                elif hand == "R":
                    print(f"\n--- L's hand ---")
                    hands["L"].showHand()
            else:
                print(f"\n--- L's hand ---")
                hands["L"].showHand()
                print(f"\n--- R's hand ---")
                hands["R"].showHand()
            
            # get which hand we are playing
            hand = input("Which hand do you want to take an action? Please input Left or Right: ")
            if hand.lower().strip() not in ["left", "right", "l", "r"]:
                print("Invalid entry.")
                continue
            
            # verify it is still active
            hand = hand[0].upper()
            player = hands[hand]
            if not player.active:
                print("That hand is no longer active.")
                continue
            
            
            while True:
                # NOTE: for now, we will not allow players to split if they are already split
                # refresh availability each loop because the commands change
                enabled_moves = ["hit", "stand", "help"]
                aliases = ["h", "s", "?"]
                # if (player.can_split()):
                #     enabled_moves.append("split")
                #     aliases.append("sp")
                # if (player.can_double()):
                #     enabled_moves.append("double down")
                #     aliases.insert("dd", -2)

                # Print what moves are available based on enabled key in moves dictionary
                print("Choose:", ", ".join(enabled_moves))
                choice = input("> ").strip().lower()

                if (choice in enabled_moves or choice in aliases):
                    if choice in ["hit", "h"]:
                        player.hit(dealer)
                    elif choice in ["stand", "s"]:
                        player.stand()
                    # elif choice in ["split", "sp"]: SEE ABOVE NOTE on Line 312
                    #     player.split(self.dealer)
                    #     break
                    # elif choice in ["double down", "dd"]:
                    #    player.double_down(self.dealer)
                    #    break
                    elif choice in ["help", "?"]:
                        print(player.help(enabled_moves + aliases))
                        continue
                    else:
                        print("Gertrude smiles menacingly: 'I don't know how you got here, but this shouldn't be possible. Try again.'")
                        continue

                    print(f"\n--- {player.name}'s hand ---")
                    player.check_cards()
                    player.showHand()
                    break
                else:
                    print("Gertrude raises an eyebrow: 'That's not a valid move. Try again.'")
        
        # split turns have all been played out
        self.active = False
        self.split_hands_score = {"L": hands["L"].check_cards(), "R": hands["R"].check_cards()}
                      
    
    # can_split()
    # inputs: none
    # outputs: can_split (boolean)
    # goals: return True if both cards in self.hand are same value
    def can_split(self):
        return len(self.hand) == 2 and self.hand[0].value == self.hand[1].value and self.money - (2 * self.bets["standard"]) > -100 
        #      ^^^only have two cards  ^^^two cards of equal value                  ^^^can't split to go below -$100
    
    # resolve_bets_split()
    # inputs: none
    # outputs: none
    # goals: special bet resolve functionality for split()
    def resolve_bet_split(self, dealerScore):
        
        for hand in ["Left", "Right"]:
            score = self.split_hands_score[hand[0]]
            
            if score > 21:
                print(f"{hand} hand busts!")
                self.money -= self.bets["standard"]
            elif dealerScore > 21:
                print(f"Dealer busts. {hand} wins!")
                self.money += self.bets["standard"]
            elif score > dealerScore:
                print(f"{hand} hand beat dealer.")
                self.money += self.bets["standard"]
            elif dealerScore > score:
                print(f"Dealer beats {hand} hand.")
                self.money -= self.bets["standard"]
            else:
                print(f"{hand} hand ties with dealer.")
            
        self.bets["standard"] = 0
        self.split_hands_score = { }
        
        return
        
    
class Gertrude(Player):
    def gertTurn(self, dealer):
        while True:
            curr_score = super().check_cards()
            if curr_score >= 17: #the dealer can't hit if their score is 17 or more
                return curr_score
            else: #the dealer needs to hit if their score is less than 17
                super().hit(dealer, True)