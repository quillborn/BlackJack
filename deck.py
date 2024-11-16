import random

class Deck:
    def __init__(self, shuffle_rate, decks):
        self.cards = []
        self.original_size = 0  # To store the original deck size
        self.shuffle_rate = shuffle_rate
        self.number_of_decks = decks

    def initialize_deck(self):
        """Initialize the deck with a specified number of decks."""
        add_deck = [
            "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
            "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
            "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
            "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"
        ]
        
        self.cards = []
        for _ in range(self.number_of_decks):
            self.cards.extend(add_deck)

    def deal(self, player_list, dealer):
        # Check if deck needs reshuffling before dealing a card
        # print(self.original_size)
        shuffle_percent = self.shuffle_rate * 0.01
        # print(shuffle_percent)
        shuffle_threshold = (self.original_size * shuffle_percent)
        # print(shuffle_threshold)
        if len(self.cards) <= shuffle_threshold:
            print("Reshuffling the deck...")
            self.initialize_deck()  # Reinitialize the deck
            
            for player in player_list:
                for hand in player.hands:
                    for card in hand.contents:
                        self.cards.remove(card)
                        # print(f"Card removed: {card}")
            
            for card in dealer.hands.contents:
                self.cards.remove(card)
                # print(f"Card removed: {card}")
        
        # Deal a card from the deck
        selected_card = random.choice(self.cards)
        self.cards.remove(selected_card)
        return selected_card

    def deal17(self, dealer_hand, dealer, player_list):
        """Deal cards until the dealer's hand value reaches or exceeds 17."""
        
        while dealer_hand.hand_value < 17:
            card = self.deal(player_list, dealer)
            dealer_hand.add_card(card, self)

        # Final card dealt (already handled by deal17 logic, can be removed if unnecessary)
        selected_card = random.choice(self.cards)
        self.cards.remove(selected_card)
        return selected_card

    def card_value(self, card):
        value = card_dict[card]
        return value

card_dict = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}
