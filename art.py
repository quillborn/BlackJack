logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

























     
# ############### Blackjack Project #####################

# #Difficulty Normal 😎: Use all Hints below to complete the project.
# #Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# #Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# #Difficulty Expert 🤯: Only use Hint 1 to complete the project.

# ############### Our Blackjack House Rules #####################

# ## The deck is unlimited in size. 
# ## There are no jokers. 
# ## The Jack/Queen/King all count as 10.
# ## The Ace can count as 11 or 1.
# ## Use the following list as the deck of cards:
# ## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# ## The cards in the list have equal probability of being drawn?
# ## Cards are not removed from the deck as they are drawn?
# ## The computer is the dealer.

# ##################### Hints #####################

# #Hint 1: Go to this website and try out the Blackjack game: 
# #   https://games.washingtonpost.com/games/blackjack/
# #Then try out the completed Blackjack project here: 
# #   https://appbrewery.github.io/python-day11-demo/

# import random
# from assets import buy_in, place_bet, deck, deck_dict, ace_check, bust_or_blackjack, dealer_reveal


# #welcome to the game!
# print("welcome to Black Jack!")

# #set up the balance via a buy_in
# balance = (buy_in())

# #set up how much the user wants to bet on round 1 via place_bet
# #and update our player's balance

# ###########################################################################################
# # #set up how many decks the user would like to play with 
# # # At the moment there are 3 instances of code that removes cards from the deck 
# # # that have been commented out to create an infinite deck
# # while True:
# #   try:
# #     num_of_decks = int(input("how many decks will we be playing with?"))
# #     for i in range(num_of_decks - 1):
# #       deck.extend(deck)
# #     break

# #   except:
# #     print("invalid input")
# ###########################################################################################

# #below we ser up the bot's hand and the player's hand for the start of a new round
# new_round = True
# while new_round == True:

#   #prior to setting up the bet, we need to check if the player has lost the game.
#   #we do so by seeing if the players balance is 0 prior to placing a bet.
#   if balance == 0:
#     print("you have lost all your money. game over.")
#     break

#   #set up how much the user wants to bet on round 1 via place_bet
#   #and update our player's balance
#   bet = (place_bet(balance))
#   balance -= bet
#   print(F"bet:{bet}")
#   print(F"balance:{balance}")

#   #The Player and the Dealer will both have a hand (list) where we will store append cards that are removed from our deck list
#   player_hand = []
#   dealer_hand = []

#   #here we deal the first hands to the player and the dealer
#   for initial_deal in range(2):

#     player_selected_card = random.choice(deck)
#     # deck.remove(player_selected_card)
#     player_hand.append(player_selected_card)

#     dealer_selected_card = random.choice(deck)
#     # deck.remove(dealer_selected_card)
#     dealer_hand.append(dealer_selected_card)

# #This While loop will evaluate the player and dealers scores and determine if there is a winner, loser, or a draw each time a card is dealt.
#   calculateing_win_cond = True
#   while calculateing_win_cond:
#     #set the hand values 
#     #they will be recalculated each time a card is dealt
#     dealer_hand_value = 0
#     player_hand_value = 0
#     #Here we calculate the value of both hands
#     for card in player_hand:
#       player_hand_value += int(deck_dict[card])

#     for card in dealer_hand:
#       dealer_hand_value += int(deck_dict[card])

#     #here we asses if the player has a hand larger than 21 and if this can be avoided since they 
#     #may have an ace
#     player_hand_value = ace_check(player_hand, player_hand_value)
#     dealer_hand_value = ace_check(dealer_hand, dealer_hand_value)

#     #this is representing the dealers second to last card
#     dstlc = (len(dealer_hand)-1)
#     #this sets up the value of the dealers hand minus the most recent card (facedown)
#     known_value_dealer_hand = dealer_hand_value - deck_dict[dealer_hand[(len(dealer_hand)-1)]]

#     #here we print the player's hand and the dealer's first card
#     print(f"\n\nYour hand:{', '.join(player_hand)} ({player_hand_value})\n")
#     print(f"Dealer hand:{', '.join(dealer_hand[0:dstlc])},??? ({known_value_dealer_hand})\n")


#     #here we check to now see if the player has blackjack
#     bust_or_blackjack(player_hand_value)
#     if bust_or_blackjack(player_hand_value) == "blackjack":
#       dealer_reveal(dealer_hand, dealer_hand_value)
#       print("BlackJack! You win!")
#       balance += (bet * 2.5)
#       print(F"\nbalance:{balance}")
#       break

#     elif bust_or_blackjack(player_hand_value) == "bust":
#       dealer_reveal(dealer_hand, dealer_hand_value)
#       print("Bust! You lose!")
#       print(F"\nbalance:{balance}")
#       break


#     bust_or_blackjack(known_value_dealer_hand)
#     if bust_or_blackjack(known_value_dealer_hand) == "blackjack":
#       dealer_reveal(dealer_hand, dealer_hand_value)
#       print("Dealer BlackJack! You lose!")
#       print(F"\nbalance:{balance}")
#       break

#     elif bust_or_blackjack(known_value_dealer_hand) == "bust":
#       dealer_reveal(dealer_hand, dealer_hand_value)
#       print("Dealer bust! You win!")
#       balance += (bet * 2.5)
#       print(F"\nbalance:{balance}")
#       break

# #here we prompt the player to hit or stand base off of curret hand values
#     hit_or_stand = input(f"\nYou have {player_hand_value} in your hand. The Dealer shows {known_value_dealer_hand}.\nWould you like to hit or stand?").lower()

# #here the player has seleced to hit and we add a card to their hand
#     if hit_or_stand[:1] == "h":
#       player_selected_card = random.choice(deck)
#       # deck.remove(player_selected_card)
#       player_hand.append(player_selected_card)

# #here if the player has selected to stand, the dealer then continues to remove cards from the deck and add them to their hand until the dealer has a hand value of 17 or greater
#     elif hit_or_stand[:1] == "s":
#       if dealer_hand_value < 17:
#         while dealer_hand_value < 17:

#           dealer_selected_card = random.choice(deck)
#           # deck.remove(dealer_selected_card)
#           dealer_hand.append(dealer_selected_card)

#           dealer_hand_value = 0
#           #here we are calculating the dealer new and value #this is possibly redundant
#           for card in dealer_hand:
#             dealer_hand_value += int(deck_dict[card])
#             dealer_hand_value = ace_check(dealer_hand, dealer_hand_value)

#         #used to show player dealer's hand
#         dealer_reveal(dealer_hand, dealer_hand_value)

#         if bust_or_blackjack(dealer_hand_value) == "blackjack":
#           if dealer_hand_value == player_hand_value:
#             print("Push")
#             balance += bet
#             print(F"\nbalance:{balance}")
#           elif dealer_hand_value > player_hand_value:
#             print("Dealer wins!")
#             print(F"\nbalance:{balance}")


#           break

#         elif bust_or_blackjack(dealer_hand_value) == "bust":
#           print("Dealer Bust! You win!")
#           balance += (bet * 2)
#           print(F"\nbalance:{balance}")
#           break

#         else:
#           if dealer_hand_value > player_hand_value:
#             print("Dealer wins!")
#             print(F"\nbalance:{balance}")
#           elif dealer_hand_value < player_hand_value:
#             print("You win!")
#             balance += (bet * 2)
#             print(F"\nbalance:{balance}")
#           else:
#             print("Push")
#             balance += bet
#             print(F"\nbalance:{balance}")

#           break


#       elif dealer_hand_value >= 17:

#         dealer_reveal(dealer_hand, dealer_hand_value)

#         if dealer_hand_value > player_hand_value:
#           print("Dealer wins!")
#           print(F"\nbalance:{balance}")
#         elif dealer_hand_value < player_hand_value:
#           print("You win!")
#           balance += (bet * 2)
#           print(F"\nbalance:{balance}")
#         else:
#           print("Push")
#           balance += bet
#           print(F"\nbalance:{balance}")

#         break





































############### Blackjack Project #####################

#this function is used to help us ensure the user is inputing integer or float values
def isnumber(string):
  if string.replace(".","").isnumeric():
    return True
  else:
    return False



#Define how much money the player has to play with (A buy in)
def buy_in():
  while True:
    try:
      value = float(input("What is the buy in this game? $"))
      return float(value)
    except:
      print("invald input")





#Define how much player would like to bet this round.
def place_bet(balance):
  while True:
    try:
      value = float(input("How much would you like to bet this round? $"))
      if value > balance:
        print("You do not have enough money to bet that amount. Please bet a lower amount.")
        return place_bet(balance)
      else:
        return float(value)
    except:
      print("invald input")





#here we asses if the player has a hand larger than 21 and if this can be avoided since they 
#may have an ace
def ace_check(selected_hand, selected_hand_value):
  number_of_aces = selected_hand.count("A")
  if selected_hand_value > 21:
    if "A" in selected_hand:
      for ace in range(number_of_aces):
        while selected_hand_value > 21:
          selected_hand_value - 10
      return selected_hand_value
    else:
      return selected_hand_value
  else:
    return selected_hand_value





def bust_or_blackjack(selected_hand_value):
  if selected_hand_value > 21:
    return "bust"
  elif selected_hand_value == 21:
    return "blackjack"
  elif selected_hand_value == range(21):
    return "variable"
  else:
    return "continue"






def dealer_reveal(selected_hand, selected_hand_value):
  print(f"\n\nDealer hand:{', '.join(selected_hand)} \nvalue of dealer hand: {selected_hand_value}")
  bust_or_blackjack(selected_hand_value)






deck_dict = {
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

deck = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K","A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
#using something like what we see below we can modify how many decks we'll be playing with
# deck.extend(("A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K","A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K","A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K","A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"))
































