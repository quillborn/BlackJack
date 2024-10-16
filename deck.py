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
            self.cards.remove(selected_card)
            dealt_cards.append(selected_card)
        return dealt_cards
    
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




    # def deck_size(self,number_of_decks):
    #     add_deck = [
    #         "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10",
    #           "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10"
    #           , "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K",
    #           ]
    #     for n in range(number_of_decks):
    #         self.decks.append(add_deck)