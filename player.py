class Player:
    def __init__(self, name):
        self.name = name                # Name of the player
        self.balance = 0.0          # Player's balance (amount of money)
        self.hands = []                 # List to store player's hands (e.g., for card games)
        self.current_bet = 0            # Current bet amount
        
    def place_bet(self, amount):
        """Places a bet if the amount is less than or equal to the balance."""
        if amount > self.balance:
            raise ValueError(f"Bet amount of {amount} exceeds balance.")
        self.current_bet = amount
        self.balance -= amount 
    def add_hand(self, hand):
        """Adds a new hand to the player's hands."""
        self.hands.append(hand)
 
    def win_bet(self, multiplier=1):
        """Player wins the bet, balance increases by the bet amount times the multiplier."""
        winnings = self.current_bet * multiplier
        self.balance += winnings
        self.current_bet = 0  # Reset bet after win
 
    def lose_bet(self):
        """Player loses the current bet."""
        self.current_bet = 0  # Reset bet after loss
 
    def __str__(self):
        return (f"Player: {self.name}, Balance: {self.balance}, "
                f"Current Bet: {self.current_bet}, Hands: {self.hands}")
 
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