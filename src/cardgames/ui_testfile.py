import unittest

from cardgames.blackjack_ui import hand_to_ascii, card_lines

# I USED AN  INBUILT PYTHON MODULE THAT TESTS THE PARTIAL FUNCTIONS AND FUNCTIONS WITHOUT RUNNING THE WHOLE TKINTER UI. THESE ARE THE FUNCTIONS THAT BREAK OR MAKE THE PROGRAM SO IF IT WORKS THEN THE PROGRAM SHOULD WORK.
class FakeCard:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = [
            "+---------+",
            f"| {value:<2}      |",
            "|         |",
            f"|    {suit}    |",
            "|         |",
            f"|      {value:>2} |",
        ]
        self.cardBack = [
            "+---------+",
            "|#########|",
            "|#########|",
            "|#########|",
            "|#########|",
            "+---------+",
        ]
        self.shortImage = [line[:4] for line in self.image]


class FakePlayer:
    def __init__(self):
        self.hand = []
        self.knownCards = []


class TestBlackjackUIHelpers(unittest.TestCase):
    def test_card_lines_front(self):
        card = FakeCard("S", "A")
        lines = card_lines(card, known=True, short=False)
        self.assertEqual(lines, card.image)

    def test_card_lines_back(self):
        card = FakeCard("S", "A")
        lines = card_lines(card, known=False, short=False)
        self.assertEqual(lines, card.cardBack)

    def test_card_lines_short(self):
        card = FakeCard("S", "A")
        lines = card_lines(card, known=True, short=True)
        self.assertEqual(lines, card.shortImage)

    def test_hand_to_ascii_empty(self):
        player = FakePlayer()
        self.assertEqual(hand_to_ascii(player), "(no cards)")

    def test_hand_to_ascii_known_cards(self):
        player = FakePlayer()
        player.hand = [FakeCard("S", "A"), FakeCard("H", "10")]
        player.knownCards = [True, True]

        output = hand_to_ascii(player, compress=False)

        self.assertIn("+---------+", output)
        self.assertIn("| A       |", output)
        self.assertIn("| 10      |", output)

    def test_hand_to_ascii_hidden_card(self):
        player = FakePlayer()
        player.hand = [FakeCard("S", "A"), FakeCard("H", "10")]
        player.knownCards = [True, False]

        output = hand_to_ascii(player, compress=False)

        self.assertIn("|#########|", output)
        self.assertIn("| A       |", output)

    def test_hand_to_ascii_compressed(self):
        player = FakePlayer()
        player.hand = [FakeCard("S", "A"), FakeCard("H", "10"), FakeCard("D", "K")]
        player.knownCards = [True, True, True]

        output = hand_to_ascii(player, compress=True)

        self.assertTrue(isinstance(output, str))
        self.assertGreater(len(output.splitlines()), 0)


if __name__ == "__main__":
    unittest.main()
