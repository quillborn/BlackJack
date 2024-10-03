from player import Player
from player import create_players, buy_in
import random
from deck import Deck



print("welcome to Black Jack!")


deck = Deck()


#here we prompt for how many players we have in our game
while True:
  try:
    player_count = int(input("How many players are playing?"))
    if(player_count >= 1 and player_count <= 4):
      break
  except:
    print("invalid input")

print(player_count) #trouble shooting




#here we generate a list of player objects based off of how our player count
player_list = create_players(player_count)

for player in player_list: #trouble shooting
  print(player.name)
print(player_list)





#set up the balance for all players via a buy_in funtion
balance = buy_in()
for player in player_list:
    player.balance += balance
    print(F"{player.name}: {player.balance}")
    



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

        print(player.hands)


    break