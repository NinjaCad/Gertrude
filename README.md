Here’s the complete **README.md file content** (just paste this directly into a file named `README.md` in your repo):

---

# 🃏 Gertrude’s Blackjack

Welcome to **Gertrude’s Blackjack**, a terminal-based Blackjack game with personality, side bets, and a dealer who *will* judge your decisions.

---

## 🎮 How to Run the Game

1. Navigate to the `src` directory:

   ```bash
   cd /app/src
   ```

2. Start the game:

   ```bash
   python -m cardgames.Games
   ```

---

## 🧠 Game Overview

This is a multiplayer Blackjack game where:

* You play against the dealer, **Gertrude**
* Supports up to **7 players**
* Each player starts with a custom amount of money
* Includes **side bets** and **dealer interactions**
* Features dynamic gameplay like **splitting** and **double down**

---

## 💰 Objective

Get as close to **21** as possible without going over, and beat the dealer’s hand.

---

## 🃏 Card Values

* Number cards (2–10) → Face value
* Face cards (J, Q, K) → 10
* Ace → 1 or 11 (automatically adjusted)

---

## 🔄 Game Flow

### 1. Setup Phase

* Choose number of players (max 7)
* Enter starting money
* Enter player names
* Choose which **side bets** to include:

  * Insurance
  * Perfect Pairs
  * 21+3
  * Tipping

---

### 2. Betting Phase

Each round:

* Players place a **standard bet**
* Optional side bets (if enabled):

  * Perfect Pairs
  * 21+3

---

### 3. Dealing Cards

* Each player and Gertrude receive **2 cards**
* Dealer shows **1 card face up**

---

### 4. Side Bet Resolution (Early)

* Perfect Pairs and 21+3 are resolved immediately after dealing

---

### 5. Insurance (Optional)

* If Gertrude shows an **Ace**, players can bet insurance

---

### 6. Player Turns

Each player takes actions:

* **Hit (h)** → Take another card
* **Stand (s)** → End turn
* **Split (sp)** → Split matching cards into two hands
* **Double Down (dd)** → Double bet, take one card, end turn
* **Help (?)** → Show rules and tips

---

### 7. Dealer Turn

* Gertrude reveals hidden card
* Must:

  * Hit until **17 or higher**
  * Stand at **17+**

---

### 8. Results

* Hands are compared against the dealer
* Bets are resolved:

  * Win → gain money
  * Lose → lose bet
  * Push → bet returned

---

### 9. End of Round

* Players can:

  * Continue playing
  * Quit the game
* Players with less than **$5** are removed

---

## 💸 Side Bets Explained

### 🛡 Insurance

* Available if dealer shows an Ace
* Bet up to half your original bet
* Wins if dealer has Blackjack

---

### 🎲 Perfect Pairs

Based on your first 2 cards:

* Colored Pair → **10:1**
* Mixed Pair → **5:1**
* Lost if you split your hand

---

### 🔺 21+3

Based on your 2 cards + dealer’s face-up card:

* Flush → **5:1**
* Straight → **10:1**
* Three of a Kind → **30:1**
* Straight Flush → **40:1**

---

### 💁 Tipping

* After winning, you may tip Gertrude
* Tipping makes her **nicer** (less brutal trash talk 👀)

---

## 🤖 Dealer: Gertrude

Gertrude isn’t just a dealer—she’s part of the experience:

* Reacts to your moves
* Roasts you when you mess up
* Becomes nicer if tipped

---

## ⚠️ Important Rules

* Minimum bet: **$5**
* You cannot go into debt
* Blackjack pays **3:2**
* Bust (>21) = automatic loss
* Split creates two independent hands
* Double Down = one card only, then stand

---

## 🏁 End of Game

* Game ends when:

  * All players are broke **OR**
  * Players choose to quit

At the end:

* Total profit/loss is displayed
* Final standings are ranked
* Gertrude gives her final (very opinionated) remarks

---

## 💡 Strategy Tips

* Hit under 12
* Stand on 17+
* Double down on 10
* Split pairs (but not 10s)
* Be cautious when dealer shows 4–6
* Play aggressive when dealer shows 7+

---

## 🧩 Features

* Multiplayer support
* Side betting system
* Split & double-down mechanics
* Dynamic dealer AI
* Money tracking and leaderboard
* Interactive CLI interface

---

## 😂 Final Note

> “The house ALWAYS wins…” — Gertrude

Good luck… you’re going to need it.
