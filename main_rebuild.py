from player import Player
from player import create_players, buy_in
import random
from deck import Deck, ace_check, standard_r1
from dealer import Dealer



print("welcome to Black Jack!")


#here we generate a deck and a dealer 
#may consider adding an innit attribute such as how many decks in game
deck = Deck()
dealer = Dealer()

#here we prompt for how many players we have in our game
while True:
  try:
    player_count = int(input("How many players are playing?"))
    if(player_count >= 1 and player_count <= 4):
      break
  except:
    print("invalid input")

print(player_count) #trouble shooting




#here we generate a list of player objects based off of our player count
player_list = create_players(player_count)





#set up the balance for all players via a buy_in funtion
balance = buy_in()
for player in player_list:
    player.balance += balance
    print(F"{player.name}: {player.balance}")


#here we deal the first two cards
for player in player_list:
    hand = deck.initial_deal()
    player.add_hand(hand)





###########################################################################################
#round initiated for looping in regards to hitting?
round = 1
game_in_progress = True
while game_in_progress:

#set how much each player is betting
    for player in player_list:
       player.place_bet()

    for player in player_list:
       print(f"{player.name}: Bet({player.bet}) Remaining balance:{player.balance}")#trouble shooting
       print (f"{player.name}: {player.hands}")

#here we will add up the players hand value 
# & must firts set all hand values to 0 to recalculate per loop(hit)

    for player in player_list:
      player.hand_value = 0  # Reset the hand value for each player
      for hand in player.hands:  # Iterate through each hand
          for card in hand:  # Iterate through each card in the hand
              player.hand_value += deck.card_value(card)  # Calculate hand value
              print(player.hand_value)  # Print total hand value after calculating for each player
              print(player.hands)

# an Ace check must be performed after values are calculated to ensure that if the player has bust
# but has an ace, that the value of the ace is converted to 1 instead of 11
    for player in player_list:
       player.hand_value = ace_check(player.hands, player.hand_value)
       

#here we display the players hand and the value of said hand       
    for player in player_list:    
        print(f"{player.name}'s Hand: {', '.join(player.hands[0])} ({player.hand_value})")


##########need to add a dealer known hand print statement here

    for player in player_list:
        if round == 1:
            for hand in player.hands:
                standard_r1(player.name,deck,hand,player.hand_value)
            
            
                player.hand_value = 0  # Reset the hand value for each player
                for hand in player.hands:  # Iterate through each hand
                    for card in hand:  # Iterate through each card in the hand
                        player.hand_value += deck.card_value(card)  # Calculate hand value
                
                player.hand_value = ace_check(player.hands, player.hand_value)  # ace check
                print(f"{player.name}'s Hand: {', '.join(hand)} ({player.hand_value})")
        
          


    break
        
"""need to add in dealer's cards & values
   need to add split and double down functionality (first turn only) may be easiest to add a new player with a simillar name to the original player
   need to add loop functionality
"""
