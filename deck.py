# we are going to let the deck act as the primary brain for the program

import random


class Deck:
    def __init__(self):

        self.cards = [
            "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10"
              , "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
              ]
        
    # def initial_deal(self): #this may now be redundant 
    #     dealt_cards = []
    #     for n in range(2):
    #         selected_card = random.choice(self.cards)
    #         # selected_card = self.cards[0] to check ace check functionality
    #         self.cards.remove(selected_card)
    #         dealt_cards.append(selected_card)
    #     return dealt_cards
    
    # def deal(self):
    #     selected_card = random.choice(self.cards)
    #     self.cards.remove(selected_card)
    #     return selected_card
    
    def deal(self):
        selected_card = self.cards[0]
        # self.cards.remove(selected_card)
        return selected_card
    
    def card_value(self,card):
        value = card_dict[card]
        return value
    




def ace_check(selected_hands, selected_hand_value):
# Iterate through each hand in the player's hands
    for hand in selected_hands:
        value = selected_hand_value
        number_of_aces = hand.count("A")  # Count Aces in the current hand

        # Adjust for Aces while value is over 21 and there are Aces to adjust
        while value > 21 and number_of_aces > 0:
            value -= 10
            
            
    return value  # Return the adjusted value after processing all hands



def bust(player,hand):
    if hand.hand_value > 21:
        print(f"{player.name} has bust")
        hand.bust = True
        return True
    else:
        return False
  
def handle_hit(player, deck, hand):
    """Handle the player hitting, receiving a card, and updating the hand."""
    card = deck.deal()
    hand.add_card(card, deck)  # Use the add_card method to append and recalculate
    print(f"{player.name} hits and receives the following: {card}.\nNew Hand: {', '.join(hand.contents)} ({hand.hand_value})")

def handle_double_down(player, deck, hand):
    """Handle the player doubling bet, receiving a card, and updating the hand."""
    player.balance -= player.bet
    player.bet += player.bet
    card = deck.deal()
    hand.add_card(card, deck)  # Use the add_card method to append and recalculate
    print(f"{player.name} doubles down. bet:{player.bet} balance:{player.balance}")
    print(f"{player.name} receives the following: {card}.\nNew Hand: {', '.join(hand.contents)} ({hand.hand_value})\n")
    bust(player, hand)

def handle_split(player, deck, hand):
    """Handle the player splitting hand. Create aother hand object & remove/add cards to each hand"""
    from hand import Hand

    x = hand.contents.count(hand.contents[0])
    if x ==2:
        split_player_hand = Hand(player.name, "2nd") #new hand object generated

        split_card = hand.contents[0]
        hand.contents.remove(split_card)
        split_player_hand.contents.append(split_card)
        player.hands.append(split_player_hand)
        for hand in player.hands:
            card = deck.deal()
            hand.add_card(card, deck)  # Use the add_card method to append and recalculate
            hand.display_hand()
        # card = deck.deal()
        # hand.add_card(card, deck)  # Use the add_card method to append and recalculate
        # print(f"{player.name} doubles down. bet:{player.bet} balance:{player.balance}")
        # print(f"{player.name} receives the following: {card}.\nNew Hand: {', '.join(hand.contents)} ({hand.hand_value})\n")
        # bust(player, hand)
    else:
        print(x)





def dhs(player, deck, hand):
    """Handle the player's decision to double down, hit, or fold on the first round."""
    hand.display_hand()
    action = input(f"\n{player.name}, would you like to double down, hit, or stand?").lower()
    
    if action.startswith("h"):
        handle_hit(player, deck, hand)
        hs(player,deck,hand)
    elif action.startswith("d"):
        if player.balance < (player.bet * 2):
            print("You do not have a high enough remaining balance to double down.")
            hs(player,deck,hand)
        else:
            handle_double_down(player, deck, hand)
    elif action.startswith("s"):
        print(f"{player.name} chooses to stand.")
    else:
        print("Invalid choice. Please choose to hit, double down, or fold.")


def sdhs(player, deck, hand):
    """Handle the player's decision to double down, hit, or fold on the first round."""
    hand.display_hand()
    action = input(f"\n{player.name}, would you like to split, double down, hit, or stand?").lower()
    
    if action.startswith("h"):
        handle_hit(player, deck, hand)
        hs(player,deck,hand)
    elif action.startswith("d"):
        if player.balance < (player.bet * 2):
            print("You do not have a high enough remaining balance to double down.")
            hs(player,deck,hand)
        else:
            handle_double_down(player, deck, hand)
    elif action.startswith("st"):
        print(f"{player.name} chooses to stand.")
    elif action.startswith("sp"):
        print(f"{player.name} chooses to split hands.")
        handle_split(player, deck, hand)
    else:
        print("Invalid choice. Please choose to hit, double down, or fold.")


def hs(player, deck, hand):
    """Handle the player's decision to double down, hit, or fold on the first round."""
    if not bust(player,hand):
        hand.display_hand()
        action = input(f"\n{player.name}, would you like to hit, or stand?").lower()
        
        if action.startswith("h"):
            handle_hit(player, deck, hand)
            hs(player, deck, hand)
        
        elif action.startswith("s"):
            print(f"{player.name} chooses to stand.")
        else:
            print("Invalid choice. Please choose to hit, double down, or fold.")
    else:
        print("Action here")








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




    # def deck_size(self,number_of_decks):
    #     add_deck = [
    #         "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    #           "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10"
    #           , "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
    #           ]
    #     for n in range(number_of_decks):
    #         self.decks.append(add_deck)