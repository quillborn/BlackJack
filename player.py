

class Player:
    def __init__(self, name):
        self.name = name                # Name of the player
        self.balance = 0.0          # Player's balance (amount of money)
        self.hands = []                 # List to store player's hands (e.g., for card games)
        self.bet = 0            # Current bet amount
        self.hand_value = 0
        
    def place_bet(self):
        """Places a bet if the amount is less than or equal to the balance."""
        while True:
            try:
                value = float(input(f"Player {self.name} How much would you like to bet this round? $"))
                if value >self.balance:
                    print("You do not have enough money to bet that amount. Please bet a lower amount.")
                else:
                    self.bet = value
                    self.balance -= value 
                    break
            except:
                print("invald input")
        

    def add_hand(self, hand):
        """Adds a new hand to the player's hands."""
        self.hands.append(hand)
 
    def win_bet(self, multiplier=1):
        """Player wins the bet, balance increases by the bet amount times the multiplier."""
        winnings = self.bet * multiplier
        self.balance += winnings
        self.bet = 0  # Reset bet after win
 
    def lose_bet(self):
        """Player loses the current bet."""
        self.bet = 0  # Reset bet after loss
 
    def __str__(self):
        return (f"Player: {self.name}, Balance: {self.balance}, "
                f"Current Bet: {self.bet}, Hands: {self.hands}")
    
    
    # def calc_hand_value(self,player_hands, player_hand_value)
    # player_hand_value = 0  # Reset the hand value for each player
    # for hand in player_hands:  # Iterate through each hand
    #     for card in hand:  # Iterate through each card in the hand
    #         player_hand_value += deck_card_value(card)  # Calculate hand value
    

    




#additional funtions relating to player below    
    
def buy_in():
    while True:
        try:
            value = float(input("What is the buy in this game? $"))
            if value < 1:
                print("Balance must be at least $1.00")
            else:
                return value
        except:
            print("invald input")
    

    
    
def create_players(num_players):
    """creates a list of player objects"""
    players = []

    for i in range (num_players):
        name = input(f"Enter the name for Player {i + 1}: ")
        i = Player(name)
        players.append(i)
    return players





 
# # Example usage
# player = Player("Alice", 1000)
# print(player)
 
# # Place a bet and update hands
# player.place_bet(100)
# player.add_hand(['Ace of Spades', 'King of Hearts'])
# print(player)
 
# # If player wins the bet with a 2x multiplier
# player.win_bet(2)
# print(player)