def pop_card(self):
        """
        Removes the last card from the player hand and 
        returns the card object.
        """
        if not self.hand:
            return None
        
        # Remove and return the last card
        played_card = self.hand.pop()
        
        # Remove the corresponding known status to keep lists in sync
        if self.knownCards:
            self.knownCards.pop()
            
        return played_card