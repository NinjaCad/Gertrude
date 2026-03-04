import pytest
from testing_base import *

def test_player_requires_pid():
    # tests to ensure that a Player object will raise a TypeError if it is implemented without assigning a PID
    with pytest.raises(TypeError):
        Player("Prof. Lee")

def test_player_has_pid_None():
    # tests that PID can be set to None (good for development and testing period)
    p3 = Player("Dr. Chou", None)
    assert hasattr(p3, "pid")

def test_player_has_pid():
    # test that PID is stored when assigned
    p4 = Player("Dr. Kim", "random_str_8q2309ru")
    assert hasattr(p4, "pid")