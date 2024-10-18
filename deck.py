# we are going to let the deck act as the primary brain for the program and may rework this file to simple be 'BLACKJACK BRAIN'

import random

class Deck:
    def __init__(self):

        self.cards = [
            "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
              "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10"
              , "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
              ]
        
    def initial_deal(self):
        dealt_cards = []
        for n in range(2):
            selected_card = random.choice(self.cards)
            # selected_card = self.cards[0] to check ace check functionality
            self.cards.remove(selected_card)
            dealt_cards.append(selected_card)
        return dealt_cards
    
    def deal(self):
        selected_card = random.choice(self.cards)
        self.cards.remove(selected_card)
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
            number_of_aces -= 1
            
    return value  # Return the adjusted value after processing all hands
    
def standard_r1(player,deck,hand,player_hand_value):
    
    print(f"\n{player} would you like to double down, hit, or fold?")
    standard_r1 = input(f"Your Hand: {', '.join(hand)} ({player_hand_value}) :").lower()
    if standard_r1[:1] == "h":
        deal = deck.deal()
        hand.append(deal)



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