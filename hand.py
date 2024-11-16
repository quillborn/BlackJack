# to get this to work, it is likely we will need to remove our initial deal function in 
# deck and use a for range statement in the main file. This allow us to have our hand contents
#remain a single list instead of a list inside of a list. 

class Hand:
    def __init__(self, name):
        self.name = name            # Name associated with the hand
        self.contents = []           # List to hold the cards in hand
        self.hand_value = 0          # Initial hand value
        self.bust_or_blackjack = False            # Has this hand busted or hit blackjack? 
        self.position = 1
        self.turn = 1

    def add_card(self, card, deck):
        """Add a card to the hand and update the hand value."""
        self.contents.append(card)
        self.calculate_hand_value(deck)

    def calculate_hand_value(self, deck):
        from BlackJack_Brain import ace_check
        """Calculate the total value of the hand, applying Ace adjustments if necessary."""
        self.hand_value = sum(deck.card_value(card) for card in self.contents)
        self.hand_value = ace_check(self.contents, self.hand_value)  # Apply Ace adjustment

    def name_position_format(self):
        if self.position >= 2 :
            return(f"{self.name}'s hand ({self.position})")
        else: 
            return(f"{self.name}'s hand ({self.position})")

    def display_hand(self):
        """Display the hand and its total value."""
        name_position = self.name_position_format()
        print(f"\n{name_position}: {', '.join(self.contents)} ({self.hand_value})")

    def display_dealer_hand(self, deck):
            """Display the dealer's hand with the last card hidden and adjust the displayed value."""
            if len(self.contents) > 1:
                displayed_cards = self.contents[:-1] + ["???"]
                displayed_value = sum(deck.card_value(card) for card in self.contents[:-1])
                print(f"\nDealer's hand: {', '.join(displayed_cards)} ({displayed_value})")
            else:
                print("\nDealer's hand: ??? (Hidden)")



   