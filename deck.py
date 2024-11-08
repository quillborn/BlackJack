# we are going to let the deck act as the primary brain for the program

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
        
        self.cards = add_deck * self.number_of_decks

    def deal(self):
        # Check if deck needs reshuffling before dealing a card
        shuffle_percent = self.shuffle_rate * 0.01
        if len(self.cards) <= self.original_size * shuffle_percent:
            print("Reshuffling the deck...")
            self.initialize_deck(self, self.number_of_decks)  # Reinitialize the deck
        
        # Deal a card from the deck
        selected_card = random.choice(self.cards)
        self.cards.remove(selected_card)
        return selected_card
    
    # # TEST CODE
    # def deal(self):
    #     # Check if deck needs reshuffling before dealing a card
    #     shuffle_percent = self.shuffle_rate * 0.01
    #     if len(self.cards) <= self.original_size * shuffle_percent:
    #         print("Reshuffling the deck...")
    #         self.initialize_deck(self.original_size // len(set(self.cards)))  # Reinitialize the deck
        
    #     # Deal a card from the deck
    #     selected_card = self.cards[0]
    #     # self.cards.remove(selected_card)
    #     return selected_card


    def deal17(self,dealer_hand):
        """Deal cards until the hand value reaches or exceeds 17."""
        
        while dealer_hand.hand_value < 17:
            card = self.deal()
            dealer_hand.add_card(card, self)
        
        # Deal a card from the deck
        selected_card = random.choice(self.cards)
        self.cards.remove(selected_card)
        return selected_card
    

    
    def card_value(self,card):
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
    
def ace_check(hand_contents, hand_value):
    """
    Adjusts the hand value to account for Aces when the total is over 21.
    """
    number_of_aces = hand_contents.count("A")
    # Adjust the hand value for Aces if it's over 21
    while hand_value > 21 and number_of_aces > 0:
        hand_value -= 10
        number_of_aces -= 1
    return hand_value







def player_action(player, deck, hand, split_tolerance):
    if hand.hand_value == 21:
        hand.display_hand()
        bust_or_blackjack(player, hand)
    else:
        x = hand.contents.count(hand.contents[0]) # count to see how many of the player's first card they have
        if hand.turn == 1: #if this is the player's first turn we will allow them to proceed through path options specific to splitting & doubling down
            if x == 2:                                          # if we counted the players first two cards as being the same..
                if player.split_count < split_tolerance:        # and they have not already reached the maximum limit of allowed splits
                    sdhs(player, deck, hand, split_tolerance)   # then we allow them to split hands
                else:
                    hs(player, deck, hand)                      # otherwise the will only have the option to hit or stand
            else:
                dhs(player, deck, hand)                         # if it is the first turn but they do not have two and only two matching cards they may still double
        elif hand.turn > 1:
            if x == 2 and player.split_count < split_tolerance :      
                shs(player, deck, hand, split_tolerance) 
            else:
                hs(player, deck, hand)




def bust_or_blackjack(player, hand):
    if hand.hand_value > 21:
        print(f"{player.name} has bust")
        hand.bust_or_blackjack = True
        return True
    elif hand.hand_value == 21:
        print(f"{player.name} hit Blackjack!")
        player.bet *= 1.5
        hand.bust_or_blackjack = True
        return True
    else:
        return False

  
def handle_hit(player, deck, hand):
    """Handle the player hitting, receiving a card, and updating the hand."""
    card = deck.deal()
    hand.turn += 1 #counts this turn as having had an official turn at play
    hand.add_card(card, deck)  # Use the add_card method to append and recalculate
    print(f"{player.name} hits and receives the following: {card}.\nNew Hand: {', '.join(hand.contents)} ({hand.hand_value})")
    if bust_or_blackjack(player, hand) == False:
        hs(player, deck, hand)
    

def handle_double_down(player, deck, hand):
    """Handle the player doubling bet, receiving a card, and updating the hand."""
    player.remaining_balance -= player.bet
    player.bet += player.bet
    card = deck.deal()
    hand.turn += 1 #counts this turn as having had an official turn at play
    hand.add_card(card, deck)  # Use the add_card method to append and recalculate
    print(f"{player.name} doubles down. bet:{player.bet} balance:{player.remaining_balance}")
    print(f"{player.name} receives the following: {card}.\nNew Hand: {', '.join(hand.contents)} ({hand.hand_value})\n")
    bust_or_blackjack(player, hand)

def handle_split(player, deck, hand):
    """Handle the player splitting hand. Create aother hand object & remove/add cards to each hand"""
    from hand import Hand
    x = hand.contents.count(hand.contents[0])
    if x == 2:
        player.split_count +=1
        split_player_hand = Hand(player.name) #new hand object generated
        split_player_hand.position += player.split_count
        split_card = hand.contents[0]
        hand.contents.remove(split_card)
        split_player_hand.contents.append(split_card)
        player.hands.append(split_player_hand)
        for hand in player.hands:
            card = deck.deal()
            hand.turn += 1 #counts this turn as having had an official turn at play
            hand.add_card(card, deck)  # Use the add_card method to append and recalculate
            hand.display_hand()
            
    else:
        print(x)


def dhs(player, deck, hand):
    """Handle the player's decision to double down, hit, or stand on the first round."""
    while True:
        hand.display_hand()
        action = input(f"{player.name}, would you like to double down, hit, or stand? (Enter 'double', 'hit', or 'stand')").lower()
        
        if action.startswith("h"):
            handle_hit(player, deck, hand)
            break
        elif action.startswith("d"):
            if player.remaining_balance < (player.bet):
                print("You do not have a high enough remaining balance to double down.")
                hs(player, deck, hand)
                break
            else:
                handle_double_down(player, deck, hand)
                break
        elif action.startswith("s"):
            print(f"{player.name} chooses to stand.")
            break
        else:
            print("Invalid choice. Please enter 'hit', 'double', or 'stand'.")


def sdhs(player, deck, hand, split_tolerance):
    """Handle the player's decision to double down, hit, or fold on the first round."""
    while True:
        hand.display_hand()
        action = input(f"{player.name}, would you like to split, double down, hit, or stand? (Enter 'split', 'double', 'hit', or 'stand')").lower()
        
        if action.startswith("h"):
            handle_hit(player, deck, hand)
            break
        elif action.startswith("d"):
            if player.remaining_balance < (player.bet * 2):
                print("You do not have a high enough remaining balance to double down.")
                player_action(player, deck, hand)
                break
            else:
                handle_double_down(player, deck, hand)
                break
        elif action.startswith("st"):
            print(f"{player.name} chooses to stand.")
            break
        elif action.startswith("sp"):
            print(f"{player.name} chooses to split hands.")
            handle_split(player, deck, hand)
            player_action(player, deck, hand, split_tolerance)
            break
        else:
            print("Invalid choice. Please enter 'split', 'double', 'hit', or 'stand'.")


def shs(player, deck, hand, split_tolerance):
    """Handle the player's decision to double down, hit, or fold on the first round."""
    while True:
        hand.display_hand()
        action = input(f"{player.name}, would you like to split, hit, or stand? (Enter 'split', 'hit', or 'stand')").lower()
        
        if action.startswith("h"):
            handle_hit(player, deck, hand)
            break
        elif action.startswith("st"):
            print(f"{player.name} chooses to stand.")
            break
        elif action.startswith("sp"):
            print(f"{player.name} chooses to split hands.")
            handle_split(player, deck, hand)
            player_action(player, deck, hand, split_tolerance)
            break
        else:
            print("Invalid choice. Please enter 'split', 'hit', or 'stand'.")


def hs(player, deck, hand):
    """Handle the player's decision to hit or stand round."""
    while True:
        hand.display_hand()
        action = input(f"{player.name}, would you like to hit, or stand? (Enter 'hit' or 'stand')").lower()
        
        if action.startswith("h"):
            handle_hit(player, deck, hand)
            break
        elif action.startswith("s"):
            print(f"{player.name} chooses to stand.")
            break
        else:
            print("Invalid choice. Please enter 'hit' or 'stand'.")





def evaluation(player,hand,dealer_hand):
    if hand.hand_value > 21:
        player.lose()
        print(f"{player.name} bust this round Hand Value:({hand.hand_value}) Player Loses:{player.bet} Player Balance:{player.balance}")
    elif hand.hand_value == 21 and dealer_hand.hand_value != 21:
        player.win()
        print(f"{player.name} hit Blackjack! Hand Value:({hand.hand_value}) Player Wins:{player.bet} Player Balance:{player.balance}")
    elif hand.hand_value == dealer_hand.hand_value:
        if hand.hand_value == 21:
            player.win()
            print(f"{player.name} hit Blackjack! Hand Value:({hand.hand_value}) Player Wins:{player.bet} Player Balance:{player.balance}")
        else:
            print(f"{player.name} has pushed Hand Value:({hand.hand_value}) Player Wins:0.0 Player Balance:{player.balance}")
    elif hand.hand_value > dealer_hand.hand_value:
        player.win()
        print(f"{player.name} wins Hand Value:({hand.hand_value}) Player Wins:{player.bet} Player Balance:{player.balance}")
    elif hand.hand_value < dealer_hand.hand_value:
        if dealer_hand.hand_value > 21:
            player.win()
            print(f"The dealer has bust, {player.name} wins Hand Value:({hand.hand_value}) Player Wins:{player.bet} Player Balance:{player.balance}")
        else:
            player.lose()
            print(f"{player.name} loses Hand Value:({hand.hand_value}) Player Loses:{player.bet} Player Balance:{player.balance}")
    