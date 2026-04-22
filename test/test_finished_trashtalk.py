from testing_base import *

gert = Gertrude("GERTRUDE")


"""
niceGert = False examples
"""

def test_bust1(monkeypatch): #patch random.choice to always return the first element of the sequence, which is "Over 21?" for the "bust" choice
    gert.niceGert = False

    monkeypatch.setattr("random.choice", lambda seq: seq[0])

    out = gert.trashTalk("bust")
    assert "Over 21?" in out

def test_hit1(monkeypatch): 
    gert.niceGert = False

    monkeypatch.setattr("random.choice", lambda seq: seq[0])

    out = gert.trashTalk("hit")
    assert "Gertrude watches closely: 'Another hit? Bold. Questionable, but bold." in out

def test_stand1(monkeypatch):
    gert.niceGert = False
    monkeypatch.setattr("random.choice", lambda seq: seq[0])
    out = gert.trashTalk("stand")
    assert "Gertrude nods slowly: 'Standing… finally. Self-control is a skill." in out


def test_split1(monkeypatch):
    gert.niceGert = False
    monkeypatch.setattr("random.choice", lambda seq: seq[0])
    out = gert.trashTalk("split")
    assert "Gertrude’s eyes narrow: 'A split? Now you’re either clever… or about to lose twice." in out


"""
niceGert = True examples
"""


def test_bust2(monkeypatch): #patch random.choice to always return the first element of the sequence, which is "Over 21?" for the "bust" choice
    gert.niceGert = True
    monkeypatch.setattr("random.choice", lambda seq: seq[0])
    out = gert.trashTalk("bust")
    assert "Gertrude sees your cards: 'Oh that happens sometimes honey, you'll get 'em next time." in out


def test_hit2(monkeypatch):
    gert.niceGert = True
    monkeypatch.setattr("random.choice", lambda seq: seq[0])
    out = gert.trashTalk("hit")
    assert "Gertrude laughs: 'You've got some bravery hitting on that hand. I like it!" in out


def test_stand2(monkeypatch):
    gert.niceGert = True
    monkeypatch.setattr("random.choice", lambda seq: seq[0])
    out = gert.trashTalk("stand")
    assert "Gertrude nods warmly: 'Standing there is totally reasonable." in out


def test_split2(monkeypatch):
    gert.niceGert = True
    monkeypatch.setattr("random.choice", lambda seq: seq[0])
    out = gert.trashTalk("split")
    assert "Gertrude grins: 'A split? I love the confidence—let’s do it!" in out

