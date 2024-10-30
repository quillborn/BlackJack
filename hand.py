# to get this to work, it is likely we will need to remove our initial deal function in 
# deck and use a for range statement in the main file. This allow us to have our hand contents
#remain a single list instead of a list inside of a list. 
from deck import ace_check

class Hand:
    def __init__(self, name):
        self.name = name            # Name associated with the hand
        self.contents = []           # List to hold the cards in hand
        self.hand_value = 0          # Initial hand value

    def add_card(self, card, deck):
        """Add a card to the hand and update the hand value."""
        self.contents.append(card)
        self.calculate_hand_value(deck)

    def calculate_hand_value(self, deck):
        """Calculate the total value of the hand with Ace adjustments."""
        self.hand_value = sum(deck.card_value(card) for card in self.contents)
        self.hand_value = ace_check(self.contents, self.hand_value)

    def display_hand(self):
        """Display the hand and its total value."""
        print(f"{self.name}'s hand: {', '.join(self.contents)} ({self.hand_value})")