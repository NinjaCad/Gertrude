from cardgames.Card_Compare import Card

def getCard(suit, value):
    return Card(suit, value, image=[], cardBack=None)

def test_higherSuitWins():
    card1 = getCard("Clubs", 7)
    card2 = getCard("Spades", 13)
    assert card1.compare(card2) == 1

def test_lowerSuitLoses():
    card1 = getCard("Hearts", 10)
    card2 = getCard("Diamonds", 5)
    assert card1.compare(card2) == -1

def test_sameSuitTie():
    card1 = getCard("Spades", 3)
    card2 = getCard("Spades", 12)
    assert card1.compare(card2) == 0