from player import Player, create_players, buy_in
import random
from deck import Deck, ace_check, dhs
from dealer import Dealer
from hand import Hand

def calc_hand_value(hand, deck):
    """Calculate the total value of the hand."""
    hand.calculate_hand_value(deck)
    return hand.hand_value

print("Welcome to Black Jack!")

# Generate a deck and a dealer
deck = Deck()
dealer = Dealer()

# Prompt for how many players are in the game
while True:
    try:
        player_count = int(input("How many players are playing? "))
        if 1 <= player_count <= 4:
            break
    except ValueError:
        print("Invalid input, please enter a number between 1 and 4.")

print(f"Player count: {player_count}")

# Generate a list of player objects based on the player count
player_list = create_players(player_count)

# Set up the balance for all players via a buy_in function
balance = buy_in()
for player in player_list:
    player.balance += balance
print(f"All Player's Balance's set to: {player.balance}\n")

# Generate hand objects for players to hold cards
for player in player_list:
    player_hand = Hand(player.name)
    player.hands.append(player_hand)  # Attach the hand to the player

    # Deal two cards to each player
    for _ in range(2):
        card = deck.deal()
        player_hand.add_card(card, deck)

#<-------------------------------------------------------- Pick up here. replace initial_deal with deal and a for in range of 2 statement 
#                                                          we have to replace any instance of player.hand with our hand objects. This allows us to have indivual hands with different contents & values (for split)




###########################################################################################
#round initiated for looping in regards to hitting?
round = 1
game_in_progress = True

while game_in_progress:

    # Set each player's bet for the round
    for player in player_list:
        player.place_bet()
        print(f"{player.name}: Bet({player.bet}) Remaining balance: {player.balance}\n")

    # Display each player's hand with its total value after Ace adjustment
    print("Hands Dealt...")
    for player in player_list:
        for hand in player.hands:
            hand.display_hand()

    # Dealer's known hand print statement here (to be implemented)

    # Special handling for the first round of play
    if round == 1:
        for player in player_list:
            for hand in player.hands:
                dhs(player, deck, hand)

    # Break the loop here for demonstration purposes; adjust based on game continuation conditions
    break
        
"""need to add in dealer's cards & values
   need to add split and double down functionality (first turn only) may be easiest to add a new player with a simillar name to the original player
   need to add loop functionality
"""
