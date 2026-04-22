import random
import math
from cardgames.Card import Card

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
        self.bets = {"standard": 0.0, "insurance": 0.0, "pairs": 0.0, "21+3": 0.0}
        self.niceGert = False
        self.blackjack_bonus_applied = False


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
        print(f"--- {self.name}'s hand ---")
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
        self.blackjack_bonus_applied = False
        
    # stand()
    # inputs: none
    # outputs: none
    # goal: change self.active to false when player stands so they can no longer make moves
    def stand(self):
        self.active = False
    
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
            self.bust()
            return total_score

        if total_score == 21:
            self.active = False
            if not self.blackjack_bonus_applied:
                self.bets["standard"] = math.ceil(self.bets["standard"] * 2.5)
                self.blackjack_bonus_applied = True

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
        # Player cannot hit after standing, busting, or reaching 21.
        if not self.active or self.check_cards() >= 21:
            self.active = False
            return None

        # hit() now goes through dealer 
        deck = dealer.deck

        if deck.size <= 0:
            # we can change this to endgame() function when we come across that in future sprints
            raise RuntimeError("Deck is empty.")

        card = deck.getCard()
        self.addCard(card, isKnown)
        self.check_cards()
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
  - Double Down: Double bet but take 1 additionally card and end your turn
  - Split: If you have 2 matching cards at the start of your turn, split into 2 hands

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
  - Pays extra -> 3:2

SIDE BETS:
  - Insurance:
      - You can bet up to half your original bet that the dealers face down card will be worth 10 if their face up card is an Ace
  - Perfect Pairs:
      - You can bet on what your starting hand will be and will get payed extra
        - Colored Pairs -> 10:1
        - Mixed Pairs -> 5:1
  - 21+3:
      - You can bet on what your starting hand and the face card of the dealer will be and will get paid extra
        - Flush -> 5:1
        - Straight -> 10:1
        - Three of a Kind -> 30:1
        - Straight Flush -> 40:1

TIPPING THE DEALER:
  - It is proper etiquette to give some of your earnings to the dealer

HELPFUL TIPS:
  - Hit if under 12
  - Stand on 17+
  - Play aggressive if dealer has 7 or higher
  - Be cautious if dealer has 4–6
  - Double down on a hand value of 10
  - Split whenever possible but not at hand value 20
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
    # Add/replace Gertrude.trashTalk with this version.
# Assumes you already have: import random
# (If you don't, add `import random` at the top of the file.)

    def trashTalk(self, event="hit"):
        """
        event: "hit", "stand", "split", "bust"
        Returns a formatted string (with newlines) to print.
        """
        if self.niceGert is False:
            lines_by_event = {
                "hit": [
                    "Gertrude watches closely: 'Another hit? Bold. Questionable, but bold.'",
                    "Gertrude smirks: 'Ah yes, the classic strategy: ignore the number 21.'",
                    "Gertrude tilts her head: 'You know “hit” isn’t a personality trait, right?'",
                    "Gertrude grins: 'You hit like 21 is just a suggestion.'",
                ],
                "stand": [
                    "Gertrude nods slowly: 'Standing… finally. Self-control is a skill.'",
                    "Gertrude raises an eyebrow: 'You’re done? I was just starting to worry you could count.'",
                    "Gertrude shrugs: 'Standing is fine. Fear is a valid strategy.'",
                    "Gertrude smiles: 'Stopping early—how responsible. I’m almost proud.'",
                ],
                "split": [
                    "Gertrude’s eyes narrow: 'A split? Now you’re either clever… or about to lose twice.'",
                    "Gertrude chuckles: 'Splitting—because losing once wasn’t exciting enough.'",
                    "Gertrude leans in: 'Two hands, double the decisions. This should be entertaining.'",
                ],
                "bust": [
                    "Gertrude clicks her tongue: 'Over 21? That’s not bravery—that’s bad math.'",
                    "Gertrude sighs: 'If you wanted to bust, you could’ve just said so.'",
                    "Gertrude laughs softly: 'And *that* is why we don’t get greedy.'",
                    "Gertrude smirks: 'Busted. The house appreciates your generous donation.'",
                    "Gertrude adjusts her sleeves: 'I’ll mark that down as: “Player vs. Basic Arithmetic.”'",
                ],
            }
        else:
            lines_by_event = {
                "hit": [
                    "Gertrude laughs: 'You've got some bravery hitting on that hand. I like it!'",
                    "Gertrude smiles: 'Alright honey, let’s see what the next card brings.'",
                    "Gertrude nods: 'Sometimes you have to take the chance—respect.'",
                ],
                "stand": [
                    "Gertrude nods warmly: 'Standing there is totally reasonable.'",
                    "Gertrude smiles: 'Good call. No need to force it.'",
                ],
                "split": [
                    "Gertrude grins: 'A split? I love the confidence—let’s do it!'",
                    "Gertrude nods: 'Okay! Two hands gives you more chances.'",
                ],
                "bust": [
                    "Gertrude sees your cards: 'Oh that happens sometimes honey, you'll get 'em next time.'",
                    "Gertrude pats the table: 'Aw, unlucky. Shake it off—we go again next round.'",
                    "Gertrude sighs kindly: 'Oof. That one hurt. You were close though.'",
                ],
            }

        # fallback if an unknown event comes in
        lines = lines_by_event.get(event) or lines_by_event["hit"]
        return "\n" + random.choice(lines) + "\n"
        
    
    
    def bet(self, type):
        # GERT-30 call trashtalk when player makes a bet
        
        while True: # while loop guarantees valid input
            # Getting players money
            if (type == "pairs"):
                bet = input(f"{self.name}, you have ${self.money}. How much do you want to bet for perfect pairs? ").strip()
            elif (type == "21+3"):
                bet = input(f"{self.name}, you have ${self.money}. How much do you want to bet for 21+3? ").strip()
            elif (type == "insurance"):
                bet = input(f"{self.name}, you previously bet ${self.bets['standard']}. You can bet up to half for insurance! How much would you like to bet? ").strip()
            else:
                bet = input(f"{self.name}, you have ${self.money}. How much do you want to bet? ").strip()
            
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
            
            elif self.money - self.bet_totals() - bet < 0: # guarantee player doesn't go more than $0 in debt
                print(f"You cannot go in debt. Be responsible!")
                continue
            
            else: # if all checks are passed, set bet and break loop
                    
                self.bets[type] = bet
                break
            
        return
    
    #Gert-54 checkBankrupt()
    def checkBankrupt(self):
        if self.money < 5:
            print(f"{self.name}, you are so broke that we had to remove you from the game hahahaha")
            self.active = False

    # helper method to check if enough money is leftover to make new bets
    def bet_totals(self):
        
        total = 0
        for key in self.bets.keys():
            total += self.bets[key]
            
        return total
            
    
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
                if self.bets[bet] != 0:
                    self.money += self.bets[bet]
                    print(f"You made ${self.bets[bet]} on your {bet} bet!")
                    print(f"Your new total is ${self.money}\n")
                    self.tipDealer() #the player won the round so tipDealer() is called to see if they want to tip the dealer
            else:
                self.money -= self.bets[bet]
             
                if self.bets[bet] != 0:
                    print(f"You lost ${self.bets[bet]} on your {bet} bet")
                    print(f"Your new total is ${self.money}\n")
                
            self.bets[bet] = 0
        
        #GERT-54 putting bankrupt checker into resolve_bet()
        self.checkBankrupt 
        return
    
    def tipDealer(self):
        while True:
            print(f"{self.name}, you have ${self.money}.")
            self.tipChoice = input("Do you want to tip the dealer? (y/n) ").strip().lower()
            if self.tipChoice == "y":
                while True:
                    try:
                        self.tipAmt = int(input("How much do you want to tip? (integer value only) ").strip())
                        if self.tipAmt > self.money:
                            print("You don't have that much money! Try again.")
                        elif self.tipAmt <= 0:
                            print("That's not a real tip amount! Try again. ")
                        else:
                            break
                    except ValueError:
                        print("That is not an integer value! Try again")
                    
                self.money -= self.tipAmt
                print("Gertrude smiles warmly: Thanks for the tip sweetie! ")
                self.niceGert = True    
                break

            elif self.tipChoice == "n":
                print("Gertrude looks at you blankly...")
                break

            else:
                print("Not a valid answer, try again.")
        return 


    # GERT-32 insurance()
    # inputs: none
    # outputs: none
    # goals: get the users bet and assign it to self.bets["insurance"]. make sure bet input is valid.
    def insurance(self, gert):
        if gert.hand[0].value == 1 and gert.hand[1].value >= 10: #Checking for Ace! 
            print(f'{self.name}, you won ${self.bets["insurance"]} from your bet because gertrude got a blackjack!')
            return True  
        else:
            print(f'{self.name}, you lost ${self.bets["insurance"]} from your bet because gertrude did not get a blackjack!')
            return False  
    
    # GERT-40 perfectPairs()
    # inputs: none
    # outputs: True or False based on if the player won the bet
        # Colored pair -> 10:1
        # Mixed pair -> 5:1
    # goals: check self.hand for mixed or colored pair
    def perfectPairs(self):
        # Requirements
        if len(self.hand) == 2:
            if self.hand[0].value == self.hand[1].value:
                # Check if it's the same color ((spades and clubs == black) and (hearts and diamonds == red)
                if (self.hand[0].suit in ["S", "C"] and self.hand[1].suit in ["S", "C"]) or (self.hand[0].suit in ["H", "D"] and self.hand[1].suit in ["H", "D"]):
                    self.bets["pairs"] *= 10
                    print(f'{self.name}, you won ${self.bets["pairs"]} from your ${self.bets["pairs"] / 10} bet because you got a colored pair!')
                else:
                    self.bets["pairs"] *= 5
                    print(f'{self.name}, you won ${self.bets["pairs"]} from your ${self.bets["pairs"] / 5} bet because you got a mixed pair!')
                return True
        print(f'{self.name}, you lost ${self.bets["pairs"]} from your bet because you got no matches!')
        return False
    
    # GERT-41 twentyone()
    # inputs: dealers top card
    # outputs: True/False based on whether or not there is a flush, straight, three of a kind, and straight flush
        # Flush -> 5:1
        # Straight -> 10:1
        # Three of a Kind -> 30:1
        # Straight Flush -> 40:1
    # goals: check self.hand for flush, straight, three of a kind, and straight flush
    def twentyone(self, dealersCard = None):
        # Requirements
        if dealersCard is not None and len(self.hand) == 2:
            # Get the three cards
            c1, c2, c3 = self.hand[0], self.hand[1], dealersCard

            # Same suit
            is_flush = (c1.suit == c2.suit == c3.suit)
            # Same value
            is_three_kind = (c1.value == c2.value == c3.value)
            
            # List of values
            vals = [c1.value, c2.value, c3.value]

            # Sorted values list but A has a value of 1
            def ranks_with_ace_low(vs):
                return sorted(vs)

            # Sorted value list but A(1) has a value of 14
            def ranks_with_ace_high(vs):
                return sorted([14 if v == 1 else v for v in vs])

            # Find if it's a straight
            def is_consecutive(rs):
                return rs[0] + 1 == rs[1] and rs[1] + 1 == rs[2]

            is_straight = is_consecutive(ranks_with_ace_low(vals)) or is_consecutive(ranks_with_ace_high(vals))

            is_straight_flush = is_straight and is_flush

            # Payouts
            if is_straight_flush:
                self.bets["21+3"] *= 40
                print(f'{self.name}, you won ${self.bets["21+3"]} from your ${self.bets["21+3"] / 40} bet because you got a straight flush!')
            elif is_three_kind:
                self.bets["21+3"] *= 30
                print(f'{self.name}, you won ${self.bets["21+3"]} from your ${self.bets["21+3"] / 30} bet because you got a three of a kind!')
            elif is_straight:
                self.bets["21+3"] *= 10
                print(f'{self.name}, you won ${self.bets["21+3"]} from your ${self.bets["21+3"] / 10} bet because you got a straight!')
            elif is_flush:
                self.bets["21+3"] *= 5
                print(f'{self.name}, you won ${self.bets["21+3"]} from your ${self.bets["21+3"] / 5} bet because you got a flush!')
            else:
                print(f'{self.name}, you lost ${self.bets["21+3"]} from your bet because you got no matches!')
                return False
            return True
        else:
            return False

    # GERT-15 split()
    # inputs: dealer (Dealer object), gertrude (Gertrude object)
    # outputs: none (may change)
    # goals: create two subhands that can each play in any order, by splitting the current hand
    #        play each hand until completion (aka stand or bust)
    #        set self.active to false
    #        to avoid messing with round() or main() structure in Games.py, all split functionality
    #        will be completely handled here
    def split(self, game):
        
        rightHand = Player(f"{self.name}'s right hand")
        rightHand.addCard(self.hand.pop(), True)
        
        self.name = f"{self.name}'s left hand"
        rightHand.bets["standard"] = self.bets["standard"]
        
        playerIndex = game.playerList.index(self)
        game.playerList.insert(playerIndex + 1, rightHand)
        
        self.hit(game.dealer)
        
    
    # can_split()
    # inputs: none
    # outputs: can_split (boolean)
    # goals: return True if both cards in self.hand are same value
    def can_split(self):
        return len(self.hand) == 2 and self.hand[0].value == self.hand[1].value and self.money - self.bet_totals() - self.bets["standard"] >= 0 and "hand" not in self.name
        #      ^^^only have two cards  ^^^two cards of equal value                  ^^^can't split to go below -$100                                  ^^^can't split if already split
    
    
    # can_double()
    # inputs: none
    # outputs: boolean
    # goals: return true if player can double (if they are on their first turn and have enough money)
    def can_double(self):
        return len(self.hand) == 2 and self.money - self.bet_totals() - self.bets["standard"] >= 0
        #      ^^^first turn           ^^^have enough money to double bet w/out going negative
    
    # double_down()
    # inputs: dealer (Dealer object)
    # outputs: none
    # goals: double the bet, hit, and stand
    def double_down(self, dealer):
        
        self.bets["standard"] *= 2
        self.hit(dealer)
        self.stand()
        
        return
        
    
class Gertrude(Player):
    def gertTurn(self, dealer):
        while True:
            curr_score = super().check_cards()
            if curr_score >= 17: #the dealer can't hit if their score is 17 or more
                return curr_score
            else: #the dealer needs to hit if their score is less than 17
                super().hit(dealer, True)