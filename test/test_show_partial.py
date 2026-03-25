# test_player_show_partial_hand.py
import pytest


from Player import Player  


class DummyCard:
    def __init__(self, short_image, back):
        
        self.shortImage = short_image
        self.cardBack = back


def test_show_partial_hand_prints_shortimage_when_known(capsys):
    p = Player("Alice")
    c1 = DummyCard(short_image=["A♠"], back=["BACK"])
    c2 = DummyCard(short_image=["K♦"], back=["BACK"])

    p.addCard(c1, isKnown=True)
    p.addCard(c2, isKnown=True)

    p.show_partial_hand()
    out = capsys.readouterr().out

    assert out == "['A♠']\n['K♦']\n"


def test_show_partial_hand_prints_back_when_unknown(capsys):
    p = Player("Dealer")
    c1 = DummyCard(short_image=["A♠"], back=["BACK1"])
    c2 = DummyCard(short_image=["K♦"], back=["BACK2"])

    p.addCard(c1, isKnown=False)
    p.addCard(c2, isKnown=False)

    p.show_partial_hand()
    out = capsys.readouterr().out

    assert out == "['BACK1']\n['BACK2']\n"


def test_show_partial_hand_mixed_known_and_unknown(capsys):
    p = Player("Dealer")
    c1 = DummyCard(short_image=["A♠"], back=["BACK1"])
    c2 = DummyCard(short_image=["K♦"], back=["BACK2"])
    c3 = DummyCard(short_image=["7♥"], back=["BACK3"])

    p.addCard(c1, isKnown=True)
    p.addCard(c2, isKnown=False)
    p.addCard(c3, isKnown=True)

    known_before = p.knownCards.copy()

    p.show_partial_hand()
    out = capsys.readouterr().out

    assert out == "['A♠']\n['BACK2']\n['7♥']\n"
    assert p.knownCards == known_before


def test_show_partial_hand_empty_hand_prints_nothing(capsys):
    p = Player("Empty")
    p.show_partial_hand()
    out = capsys.readouterr().out
    assert out == ""


@pytest.mark.parametrize(
    "known_flags,expected_lines",
    [
        ([True], ["['A♠']"]),
        ([False], ["['BACK']"]),
        ([True, False], ["['A♠']", "['BACK2']"]),
    ],
)
def test_show_partial_hand_parametrized(capsys, known_flags, expected_lines):
    p = Player("Param")

    cards = [
        DummyCard(short_image=["A♠"], back=["BACK"]),
        DummyCard(short_image=["K♦"], back=["BACK2"]),
    ]

    for i, flag in enumerate(known_flags):
        p.addCard(cards[i], isKnown=flag)

    p.show_partial_hand()
    out = capsys.readouterr().out

    assert out == "\n".join(expected_lines) + ("\n" if expected_lines else "")