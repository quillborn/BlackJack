############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn?
## Cards are not removed from the deck as they are drawn?
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

import random
from assets import buy_in, place_bet, deck, deck_dict, ace_check, bust_or_blackjack, dealer_reveal

from player import Player 


#welcome to the game!
print("welcome to Black Jack!")


###########################################################################################
#add multiple players?

while True:
  try:
    player_count = int(input("How many players are playing?"))
    if(player_count >= 1 and player_count <= 4):
      break
  except:
    print("invalid input")



player_inf = []

# for players in range(player_count):
#   player_dict = {
#     f"player_0{players}":[{f"hand_0{players}":[[],{f"hand_0{players}_value":0},{f"hand_0{players}_bet":0}]}],
#     f"balance_player_0{players}":0
#   }
#   player_inf.append(player_dict)

for i in range(player_count):
  player = Player(f"Player_{i}")


  player_inf.append(player)

  print(player_inf)


############################################################################################

#set up the balance via a buy_in
balance = (buy_in())
for player in player_inf:
  player.balance += balance
  print(F"{player.name}: {player.balance}")
 

#set up how much the user wants to bet on round 1 via place_bet
#and update our player's balance

###########################################################################################
# #set up how many decks the user would like to play with 
# # At the moment there are 3 instances of code that removes cards from the deck 
# # that have been commented out to create an infinite deck
# while True:
#   try:
#     num_of_decks = int(input("how many decks will we be playing with?"))
#     for i in range(num_of_decks - 1):
#       deck.extend(deck)
#     break
    
#   except:
#     print("invalid input")
###########################################################################################


#below we ser up the bot's hand and the player's hand for the start of a new round
new_round = True
while new_round == True:

  #prior to setting up the bet, we need to check if the player has lost the game.
  #we do so by seeing if the players balance is 0 prior to placing a bet.
  if balance == 0:
    print("you have lost all your money. game over.")
    break
  
  #set up how much the user wants to bet on round 1 via place_bet
  #and update our player's balance
  for players in range(player_count):
    
    player_inf[players][f"player_0{players}"][0][f"hand_0{players}"][2][f"hand_0{players}_bet"] = (place_bet(balance,(players+1)))
    player_inf[players][f"balance_player_0{players}"] -= player_inf[players][f"player_0{players}"][0][f"hand_0{players}"][2][f"hand_0{players}_bet"]

    bet = player_inf[players][f"player_0{players}"][0][f"hand_0{players}"][2][f"hand_0{players}_bet"]
    balance = player_inf[players][f"balance_player_0{players}"]
    
    print(F"\nPlayer {(players+1)} bet: {bet}")
    print(F"Player {(players+1)} balance: {balance}\n")

  #The Dealer will have a hand (list) where we will store append cards that are removed from our deck list
  
  dealer_hand = []
  #here we deal the first hands to the player and the dealer
  for initial_deal in range(2):

    for players in range(player_count):
      player_selected_card = random.choice(deck)
      deck.remove(player_selected_card)
      player_inf[players][f"player_0{players}"][0][f"hand_0{players}"][0].append(player_selected_card)

    dealer_selected_card = random.choice(deck)
    deck.remove(dealer_selected_card)
    dealer_hand.append(dealer_selected_card)

  # prints player hand
  # for players in range(player_count):
  #   X = player_inf[players][f"player_0{players}"][0][f"hand_0{players}"][0]
  #   print(f"player {(players+1)}'s hand:" + f"{X}")

#This While loop will evaluate the player and dealers scores and determine if there is a winner, loser, or a draw each time a card is dealt.
  calculateing_win_cond = True
  while calculateing_win_cond:
    #set the hand values 
    #they will be recalculated each time a card is dealt
    dealer_hand_value = 0

    #Here we calculate the value of both hands
    for players in range(player_count):
      #players hands defined
      player_inf[players][f"player_0{players}"][0][f"hand_0{players}"][1][f"hand_0{players}_value"] = 0
      selected_hand_list_players = player_inf[players][f"player_0{players}"][0][f"hand_0{players}"][0]
      
      
      for card in (selected_hand_list_players):
        #add up player values
        player_inf[players][f"player_0{players}"][0][f"hand_0{players}"][1][f"hand_0{players}_value"] += int(deck_dict[card])
        #player value set
        player_hand_value = player_inf[players][f"player_0{players}"][0][f"hand_0{players}"][1][f"hand_0{players}_value"]
        #here we asses if theres a hand larger than 21 and if this can be avoided since it may have an ace
        player_inf[players][f"player_0{players}"][0][f"hand_0{players}"][1][f"hand_0{players}_value"] = ace_check(selected_hand_list_players, player_hand_value)
        
       
          
    #prints players hands + Value of hand
    for players in range(player_count):
      X = ', '.join(player_inf[players][f"player_0{players}"][0][f"hand_0{players}"][0])
      Y = player_inf[players][f"player_0{players}"][0][f"hand_0{players}"][1][f"hand_0{players}_value"]
      print(f"player {(players+1)}'s hand: " + f"{X}" + f" ({Y})")
    
    for card in dealer_hand:
      dealer_hand_value += int(deck_dict[card])
      #here we asses if theres a hand larger than 21 and if this can be avoided since it may have an ace
      dealer_hand_value = ace_check(dealer_hand, dealer_hand_value)
      
    #this is representing the dealers second to last card
    dstlc = (len(dealer_hand)-1)
    #this sets up the value of the dealers hand minus the most recent card (facedown)
    known_value_dealer_hand = dealer_hand_value - deck_dict[dealer_hand[(len(dealer_hand)-1)]]
    print(f"Dealer hand: {', '.join(dealer_hand[0:dstlc])}, ??? ({known_value_dealer_hand})\n")
      
   
    #here we check to now see if the player has blackjack
    bust_or_blackjack(player_hand_value)
    if bust_or_blackjack(player_hand_value) == "blackjack":
      dealer_reveal(dealer_hand, dealer_hand_value)
      print("BlackJack! You win!")
      balance += (bet * 2.5)
      print(F"\nbalance:{balance}")
      break
      
    elif bust_or_blackjack(player_hand_value) == "bust":
      dealer_reveal(dealer_hand, dealer_hand_value)
      print("Bust! You lose!")
      print(F"\nbalance:{balance}")
      break
      
      
    bust_or_blackjack(known_value_dealer_hand)
    if bust_or_blackjack(known_value_dealer_hand) == "blackjack":
      dealer_reveal(dealer_hand, dealer_hand_value)
      print("Dealer BlackJack! You lose!")
      print(F"\nbalance:{balance}")
      break

    elif bust_or_blackjack(known_value_dealer_hand) == "bust":
      dealer_reveal(dealer_hand, dealer_hand_value)
      print("Dealer bust! You win!")
      balance += (bet * 2.5)
      print(F"\nbalance:{balance}")
      break

#here we prompt the player to hit or stand base off of curret hand values
    hit_or_stand = input(f"\nYou have {player_hand_value} in your hand. The Dealer shows {known_value_dealer_hand}.\nWould you like to hit or stand?").lower()

#here the player has seleced to hit and we add a card to their hand
    if hit_or_stand[:1] == "h":
      player_selected_card = random.choice(deck)
      # deck.remove(player_selected_card)
      player_hand.append(player_selected_card)
      
#here if the player has selected to stand, the dealer then continues to remove cards from the deck and add them to their hand until the dealer has a hand value of 17 or greater
    elif hit_or_stand[:1] == "s":
      if dealer_hand_value < 17:
        while dealer_hand_value < 17:
          
          dealer_selected_card = random.choice(deck)
          # deck.remove(dealer_selected_card)
          dealer_hand.append(dealer_selected_card)

          dealer_hand_value = 0
          #here we are calculating the dealer new and value #this is possibly redundant
          for card in dealer_hand:
            dealer_hand_value += int(deck_dict[card])
            dealer_hand_value = ace_check(dealer_hand, dealer_hand_value)

        #used to show player dealer's hand
        dealer_reveal(dealer_hand, dealer_hand_value)
        
        if bust_or_blackjack(dealer_hand_value) == "blackjack":
          if dealer_hand_value == player_hand_value:
            print("Push")
            balance += bet
            print(F"\nbalance:{balance}")
          elif dealer_hand_value > player_hand_value:
            print("Dealer wins!")
            print(F"\nbalance:{balance}")
        
          
          break

        elif bust_or_blackjack(dealer_hand_value) == "bust":
          print("Dealer Bust! You win!")
          balance += (bet * 2)
          print(F"\nbalance:{balance}")
          break

        else:
          if dealer_hand_value > player_hand_value:
            print("Dealer wins!")
            print(F"\nbalance:{balance}")
          elif dealer_hand_value < player_hand_value:
            print("You win!")
            balance += (bet * 2)
            print(F"\nbalance:{balance}")
          else:
            print("Push")
            balance += bet
            print(F"\nbalance:{balance}")

          break
        
        
      elif dealer_hand_value >= 17:
        
        dealer_reveal(dealer_hand, dealer_hand_value)
        
        if dealer_hand_value > player_hand_value:
          print("Dealer wins!")
          print(F"\nbalance:{balance}")
        elif dealer_hand_value < player_hand_value:
          print("You win!")
          balance += (bet * 2)
          print(F"\nbalance:{balance}")
        else:
          print("Push")
          balance += bet
          print(F"\nbalance:{balance}")

        break
        
     



  

  
  























