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
def place_bet(balance,player_name):
  while True:
    try:
      value = float(input(f"Player {player_name} How much would you like to bet this round? $"))
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


def Deal(player_hands_dictionary,seleted_player_hand):

  for hands in player_hands_dictionary:
    player_selected_card = random.choice(deck)
    # deck.remove(player_selected_card)
    player_hands[selected_player_hand].append(player_selected_card)

