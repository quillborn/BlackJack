from player import Player
from player import create_players, buy_in
import random
from deck import Deck, card_dict
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

for player in player_list: #trouble shooting
  print(player.name)
print(player_list)





#set up the balance for all players via a buy_in funtion
balance = buy_in()
for player in player_list:
    player.balance += balance
    print(F"{player.name}: {player.balance}")
    


###########################################################################################
#round initiated for looping in regards to hitting?
game_in_progress = True
while game_in_progress:





#set how much each player is betting
    for player in player_list:
       player.place_bet()

    for player in player_list:
       print(f"{player.name}: Bet({player.bet}) Remaining balance:{player.balance}")#trouble shooting





    for player in player_list:
        player.add_hand(deck.initial_deal())

#here we will add up the players hand value 
# & must firts set all hand values to 0 to recalculate per loop(hit)
    for player in player_list:
       player.hand_value = 0
#Calculating hand values   
    for player in player_list:
      for hand in player.hands:  # Iterate through each hand
          for card in hand:  # Iterate through each card in the hand
              player.hand_value += deck.card_value(card)
          
        
    for player in player_list:    
        print(f"{player.name}'s Hand: {', '.join(player.hands[0])} ({player.hand_value})")
        
"""need to add in dealer's cards & values
   need to add an ace check into loop to adjust value of ace if over 21
   need to add split and double down functionality (first turn only)
"""

    break