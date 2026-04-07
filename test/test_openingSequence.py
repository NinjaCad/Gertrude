from testing_base import *

#made this whole test
#------------------------------
#this is so that there is no player input and just choices
def handle_menu_choice(choice):
    if choice == "1":
        return "start"
    elif choice == "2":
        return "rules"
    elif choice == "3":
        return "quit"
    else:
        return "invalid"

def test_menu_choice_start():
    assert handle_menu_choice("1") == "start"

def test_menu_choice_invalid():
    assert handle_menu_choice("xyz") == "invalid"

def test_menu_choice_quit():
    assert handle_menu_choice("3") == "quit"

#i just want a portion of the lines
def get_opening_lines():
    return [
        "The cards are shuffled...",
        "Your opponents are ready...",
        "Time to test your luck..."
    ]

def test_opening_lines():
    lines = get_opening_lines()
    
    assert len(lines) == 3
    assert "cards are shuffled" in lines[0].lower()
#------------------------------