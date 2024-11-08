from player import create_players, buy_in
from deck import Deck, player_action, evaluation
from dealer import Dealer
from hand import Hand
from art import logo


# Final step will involve finalizing shuffle method by collecting a list of all cards currentl in play and removing them from the reinitialized deck


print(logo)
print("Welcome to Black Jack!")

#Setting cutsom values
split_tolerance = 2
max_players = 4
number_of_decks = 1
shuffle_rate = 50 # % representation

# Generate a deck & add addittional decks if prompted
deck = Deck(shuffle_rate, number_of_decks)
deck.initialize_deck()
print(deck.cards)

# Prompt for how many players are in the game
while True:
    try:
        player_count = int(input("How many players are playing? (1-4): "))
        if 1 <= player_count <= max_players:
            break
        print("Please enter a number between 1 and 4.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

print(f"Player count: {player_count}")

# Generate a list of player objects based on the player count
player_list = create_players(player_count)

# Set up the balance for all players via a buy_in function
balance = buy_in()
for player in player_list:
    player.balance += balance
    player.remaining_balance += balance
print(f"All Player's Balance's set to: {player.balance}\n")

###################################################
#round initiated for looping in regards to hitting?

while True:

    #filter our any player that have hit a balance of 0 and lost
    player_list = [player for player in player_list if player.balance > 0]

    # Check if all players have been removed
    if not player_list:
        print("All players are out of balance. Game over.")
        exit()

    # Generate hand objects for players to hold cards
    for player in player_list:
        player_hand = Hand(player.name)
        player.hands.append(player_hand)  # Attach the hand to the player

        # Deal two cards to each player
        for _ in range(2):
            card = deck.deal()
            player_hand.add_card(card, deck)

    #generate our dealer object alongside their hand & cards
    dealer_hand = Hand("Dealer")  # Generates Dealer hand object
    for x in range(2):
        card = deck.deal()
        dealer_hand.add_card(card, deck)
    dealer = Dealer(dealer_hand)    # Dealer generated second in order to use hand object in innit
    
    # Set each player's bet for the round
    for player in player_list:
        player.place_bet()
        print(f"{player.name}: Bet({player.bet}) Remaining balance: {player.remaining_balance}\n")

    # Display the dealer's hand. Players hand's are revealed one at a time for visual clarity
    print("Hands Dealt...")
    dealer_hand.display_dealer_hand(deck)

    #Decide what actions the player can take and presents them
    for player in player_list:
        for hand in player.hands:
            player_action(player, deck, hand,split_tolerance)
            
    #Dealer Draws until they have a hand value of 17 or greater and then reveals hand
    deck.deal17(dealer_hand)
    dealer_hand.display_hand()

    for player in player_list:
        for hand in player.hands:
            evaluation(player,hand,dealer_hand)

    #filter our any player that have hit a balance of 0 and lost
    player_list = [player for player in player_list if player.balance > 0]

    # Check if all players have been removed
    if not player_list:
        print("All players are out of balance. Game over.")
        exit()

    while True:
        continue_game = input("\nContinue? Y/N: ").strip().lower()

        if continue_game.startswith("y"):
            for player in player_list:
                player.reset_player()
                for hand in player.hands:
                    hand.reset_hand()
            break  # Continue to the next game loop iteration

        elif continue_game.startswith("n"):
            print("Game over. Exiting...")
            exit()  # Exit the program immediately

        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
