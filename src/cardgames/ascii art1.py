def card_art(suit, number):
    rank = str(number)
    top = "┌─────────┐"
    bottom = "└─────────┘"
    side = "│         │"
    if rank == "10":
        rank_left = rank + " " * 7
        rank_right = " " * 7 + rank
    else:
        rank_left = rank + " " * 8
        rank_right = " " * 8 + rank
    line1 = top
    line2 = f"│{rank_left}│"
    line3 = side
    line4 = f"│    {suit}    │"
    line5 = side
    line6 = f"│{rank_right}│"
    line7 = bottom
    return f"{line1}\n{line2}\n{line3}\n{line4}\n{line5}\n{line6}\n{line7}"
def main():
    cards = [
        ('A', '♣'), ('2', '♣'), ('3', '♣'), ('4', '♣'), ('5', '♣'), ('6', '♣'), ('7', '♣'), ('8', '♣'), ('9', '♣'), ('10', '♣'), ('J', '♣'), ('Q', '♣'), ('K', '♣'), 
        ('A', '♠'), ('2', '♠'), ('3', '♠'), ('4', '♠'), ('5', '♠'), ('6', '♠'), ('7', '♠'), ('8', '♠'), ('9', '♠'), ('10', '♠'), ('J', '♠'), ('Q', '♠'), ('K', '♠'), 
        ('A', '♥'), ('2', '♥'), ('3', '♥'), ('4', '♥'), ('5', '♥'), ('6', '♥'), ('7', '♥'), ('8', '♥'), ('9', '♥'), ('10', '♥'), ('J', '♥'), ('Q', '♥'), ('K', '♥'), 
        ('A', '♦'), ('2', '♦'), ('3', '♦'), ('4', '♦'), ('5', '♦'), ('6', '♦'), ('7', '♦'), ('8', '♦'), ('9', '♦'), ('10', '♦'), ('J', '♦'), ('Q', '♦'), ('K', '♦')
    ]
    for rank, suit in cards:
        print(card_art(suit, rank))
        print()  
if __name__ == "__main__":
    main()