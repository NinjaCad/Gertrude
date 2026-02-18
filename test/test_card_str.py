# Card.py __str__ test - Roman Menotti
from testing_base import * 

def test_str_logic():
    
    image_input = ["10 of Hearts", "Image Line 2"]
    card = Card("Hearts", "10", image_input, "Back")
    print(card)

    expected_short = "10 o\nImag"
    
    actual_short = card.__str__(short=True)
    print(actual_short)
    
    if actual_short == expected_short:
        print("The class correctly sliced the str")
    else:
        print(f"Got {repr(actual_short)} instead of {repr(expected_short)}")


test_str_logic()
