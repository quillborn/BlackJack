# to get this to work, it is likely we will need to remove our initial deal function in 
# deck and use a for range statement in the main file. This allow us to have our hand contents
#remain a single list instead of a list inside of a list. 

class Hand:
    def __init__(self, name, position):
        self.name = name            # Name associated with the hand
        self.contents = []           # List to hold the cards in hand
        self.hand_value = 0          # Initial hand value
        self.bust = False            # Has this hand busted or not? 
        self.position = position

    def add_card(self, card, deck):
        """Add a card to the hand and update the hand value."""
        self.contents.append(card)
        self.calculate_hand_value(deck)

    def calculate_hand_value(self, deck):
        from deck import ace_check
        """Calculate the total value of the hand with Ace adjustments."""
        self.hand_value = sum(deck.card_value(card) for card in self.contents)
        self.hand_value = ace_check(self.contents, self.hand_value)


    def name_position_format(self):
        if self.position == "2nd":
            return(f"{self.name}'s {self.position} hand")
        else: 
            return(f"{self.name}'s {self.position} hand")


    def display_hand(self):
        """Display the hand and its total value."""
        name_position = self.name_position_format()
        print(f"{name_position}: {', '.join(self.contents)} ({self.hand_value})")


   