def BlackJack(): 
    # Import
    from player import create_players, buy_in
    from deck import Deck
    from dealer import Dealer
    from hand import Hand

    # Setting custom values
    split_tolerance = 3
    max_players = 4
    number_of_decks = 1
    shuffle_rate = 50  # % representation

    # Settings Preset
    while True:
        settings = input("Would you like to modify settings before starting? Y/N: ").lower()
        if settings == "y":
            while True:
                # Display settings menu
                try:
                    print(f"Which setting would you like to change?")
                    print(f"1. Split Tolerance: {split_tolerance}")
                    print(f"2. Max Players: {max_players}")
                    print(f"3. Number of Decks: {number_of_decks}")
                    print(f"4. Shuffle Rate: {shuffle_rate}%")
                    print("5. Exit Settings")

                    setting_select = int(input("Enter the number of the setting you'd like to change: "))

                    if setting_select == 1:  # Change Split Tolerance
                        while True:
                            try:
                                x = int(input(f"How many splits would you like a player to be capable of? (currently {split_tolerance}): "))
                                if 0 <= x <= 3:
                                    split_tolerance = x
                                    print(f"Split Tolerance updated to {split_tolerance}.")
                                    break
                                print("Please enter a value between 0 and 3.")
                            except ValueError:
                                print("Invalid input. Please enter a number between 0 and 3.")

                    elif setting_select == 2:  # Change Max Players
                        while True:
                            try:
                                x = int(input(f"How many players are allowed? (currently {max_players}): "))
                                if 1 <= x <= 10:  # Adjust range as per your game's constraints
                                    max_players = x
                                    print(f"Max Players updated to {max_players}.")
                                    break
                                print("Please enter a value between 1 and 10.")
                            except ValueError:
                                print("Invalid input. Please enter a number between 1 and 10.")

                    elif setting_select == 3:  # Change Number of Decks
                        while True:
                            try:
                                x = int(input(f"How many decks should be used? (currently {number_of_decks}): "))
                                if 1 <= x <= 8:  # Adjust range as needed
                                    number_of_decks = x
                                    print(f"Number of Decks updated to {number_of_decks}.")
                                    break
                                print("Please enter a value between 1 and 8.")
                            except ValueError:
                                print("Invalid input. Please enter a number between 1 and 8.")

                    elif setting_select == 4:  # Change Shuffle Rate
                        while True:
                            try:
                                x = int(input(f"What should the shuffle rate be? (currently {shuffle_rate}%): "))
                                if 0 <= x <= 50:  # Adjust range as needed
                                    shuffle_rate = x
                                    print(f"Shuffle Rate updated to {shuffle_rate}%.")
                                    break
                                print("Please enter a value between 0 and 50.")
                            except ValueError:
                                print("Invalid input. Please enter a number between 0 and 50.")

                    elif setting_select == 5:  # Exit the settings menu
                        print("Exiting settings menu.")
                        break

                    else:
                        print("Invalid option. Please select a number between 1 and 5.")

                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 5.")
        elif settings == "n":
            break
        else:
            print("Invalid input")    

    # Generate a deck & add additional decks if prompted
    deck = Deck(shuffle_rate, number_of_decks)
    deck.initialize_deck()
    deck.original_size = len(deck.cards)

    # Prompt for how many players are in the game
    while True:
        try:
            player_count = int(input(f"\nHow many players are playing? (1-{max_players}): "))
            if 1 <= player_count <= max_players:
                break
            print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"Player count: {player_count}")

    # Generate a list of player objects based on the player count
    player_list = create_players(player_count)

    # Generate the dealer object and hand
    dealer_hand = Hand("Dealer")
    dealer = Dealer(dealer_hand)

    # Set up the balance for all players via a buy_in function
    balance = buy_in()
    for player in player_list:
        player.balance += balance
        player.remaining_balance += balance
    print(f"All Player's Balances set to: ${player.balance:.2f}\n")

    while True:

        # Filter out any player that has hit a balance of $0 and lost
        player_list = [player for player in player_list if player.balance > 0]

        # Check if all players have been removed
        if not player_list:
            print("All players are out of balance. Game over.")
            break

        # Generate hand objects for players to hold cards
        for player in player_list:
            player_hand = Hand(player.name)
            player.hands.append(player_hand)  # Attach the hand to the player

            # Deal two cards to each player
            for _ in range(2):
                card = deck.deal(player_list, dealer)
                player_hand.add_card(card, deck)

        # Deal two cards to the dealer
        for _ in range(2):
            card = deck.deal(player_list, dealer)
            dealer_hand.add_card(card, deck)

        # Set each player's bet for the round
        for player in player_list:
            player.place_bet()
            print(f"{player.name}: Bet(${player.bet:.2f}) Remaining balance: ${player.remaining_balance:.2f}\n")

        # Display the dealer's hand. Players hands are revealed one at a time for visual clarity
        print("Hands Dealt...")
        dealer_hand.display_dealer_hand(deck)

        # Decide what actions the player can take and present them
        for player in player_list:
            for hand in player.hands:
                player_action(player, deck, hand, split_tolerance, player_list, dealer)
                
        # Dealer draws until they have a hand value of 17 or greater and then reveals the hand
        deck.deal17(dealer_hand, dealer, player_list)
        dealer_hand.display_hand()

        for player in player_list:
            for hand in player.hands:
                evaluation(player, hand, dealer_hand)

        # Filter out any player that has hit a balance of $0 and lost
        player_list = [player for player in player_list if player.balance > 0]

        # Check if all players have been removed
        if not player_list:
            print("All players are out of money. Game over.")
            for player in player_list:
                player.reset_player()
                del player
            dealer.reset_dealer()
            del dealer
            break

        while True:
            continue_game = input("\nContinue? Y/N: ").strip().lower()

            if continue_game.startswith("y"):
                for player in player_list:
                    player.reset_player()
                dealer.reset_dealer()
                break  # Continue to the next game loop iteration

            elif continue_game.startswith("n"):
                for player in player_list:
                    player.reset_player()
                    del player
                dealer.reset_dealer()
                del dealer
                print("Game over.")
                return  # Exit the game

            else:
                print('Invalid input. Please enter "Y" or "N".')
        if continue_game.startswith("y"):
            continue
        else:
            break

        


def ace_check(hand_contents, hand_value):
    """
    Adjusts the hand value to account for Aces when the total is over 21.
    """
    number_of_aces = hand_contents.count("A")
    # Adjust the hand value for Aces if it's over 21
    while hand_value > 21 and number_of_aces > 0:
        hand_value -= 10
        number_of_aces -= 1
    return hand_value

def player_action(player, deck, hand, split_tolerance, player_list, dealer):
    if hand.hand_value == 21:
        hand.display_hand()
        bust_or_blackjack(player, hand)
    else:
        x = hand.contents.count(hand.contents[0])  # count to see how many of the player's first card they have
        if hand.turn == 1:  # if this is the player's first turn, we allow them to proceed through path options
            if x == 2:  # if we counted the player's first two cards as being the same
                if player.split_count < split_tolerance:  # and they have not already reached the maximum limit of allowed splits
                    sdhs(player, deck, hand, split_tolerance, player_list, dealer)  # then we allow them to split hands
                else:
                    hs(player, deck, hand, player_list, dealer)  # otherwise they only have the option to hit or stand
            else:
                dhs(player, deck, hand, player_list, dealer)  # if it's the first turn but no matching cards, they may still double
        elif hand.turn > 1:
            if x == 2 and player.split_count < split_tolerance:
                shs(player, deck, hand, split_tolerance, player_list, dealer)
            else:
                hs(player, deck, hand, player_list, dealer)

def bust_or_blackjack(player, hand):
    if hand.hand_value > 21:
        print(f"{player.name} has bust")
        hand.bust_or_blackjack = True
        return True
    elif hand.hand_value == 21:
        print(f"{player.name} hit Blackjack!")
        player.bet *= 1.5
        hand.bust_or_blackjack = True
        return True
    else:
        return False
  
def handle_hit(player, deck, hand, player_list, dealer):
    """Handle the player hitting, receiving a card, and updating the hand."""
    card = deck.deal(player_list, dealer)
    hand.turn += 1  # counts this turn as having had an official turn at play
    hand.add_card(card, deck)  # Use the add_card method to append and recalculate
    print(f"{player.name} hits and receives the following: {card}.\nNew Hand: {', '.join(hand.contents)} ({hand.hand_value})")
    if bust_or_blackjack(player, hand) == False:
        hs(player, deck, hand, player_list, dealer)

def handle_double_down(player, deck, hand, player_list, dealer):
    """Handle the player doubling bet, receiving a card, and updating the hand."""
    player.remaining_balance -= player.bet
    player.bet += player.bet
    card = deck.deal(player_list, dealer)
    hand.turn += 1  # counts this turn as having had an official turn at play
    hand.add_card(card, deck)  # Use the add_card method to append and recalculate
    print(f"{player.name} doubles down. bet:{player.bet} balance:{player.remaining_balance}")
    print(f"{player.name} receives the following: {card}.\nNew Hand: {', '.join(hand.contents)} ({hand.hand_value})\n")
    bust_or_blackjack(player, hand)

def handle_split(player, deck, hand, player_list, dealer):
    """Handle the player splitting hand. Create another hand object & remove/add cards to each hand"""
    from hand import Hand
    x = hand.contents.count(hand.contents[0])
    if x == 2:
        player.split_count += 1
        split_player_hand = Hand(player.name)  # new hand object generated
        split_player_hand.position += player.split_count
        split_card = hand.contents[0]
        hand.contents.remove(split_card)
        split_player_hand.contents.append(split_card)
        player.hands.append(split_player_hand)
        for hand in player.hands:
            card = deck.deal(player_list, dealer)
            hand.turn += 1  # counts this turn as having had an official turn at play
            hand.add_card(card, deck)  # Use the add_card method to append and recalculate
            hand.display_hand()
    else:
        print(x)

def dhs(player, deck, hand, player_list, dealer):
    """Handle the player's decision to double down, hit, or stand on the first round."""
    while True:
        hand.display_hand()
        action = input(f"{player.name}, would you like to double down, hit, or stand? (Enter 'double', 'hit', or 'stand')").lower()
        if action.startswith("h"):
            handle_hit(player, deck, hand, player_list, dealer)
            break
        elif action.startswith("d"):
            if player.remaining_balance < (player.bet):
                print("You do not have a high enough remaining balance to double down.")
                hs(player, deck, hand, player_list, dealer)
                break
            else:
                handle_double_down(player, deck, hand, player_list, dealer)
                break
        elif action.startswith("s"):
            print(f"{player.name} chooses to stand.")
            break
        else:
            print("Invalid choice. Please enter 'hit', 'double', or 'stand'.")

def sdhs(player, deck, hand, split_tolerance, player_list, dealer):
    """Handle the player's decision to split, double down, hit, or stand."""
    while True:
        hand.display_hand()
        action = input(f"{player.name}, would you like to split, double down, hit, or stand? (Enter 'split', 'double', 'hit', or 'stand')").lower()
        if action.startswith("h"):
            handle_hit(player, deck, hand, player_list, dealer)
            break
        elif action.startswith("d"):
            if player.remaining_balance < (player.bet * 2):
                print("You do not have a high enough remaining balance to double down.")
                player_action(player, deck, hand, split_tolerance, player_list, dealer)
                break
            else:
                handle_double_down(player, deck, hand, player_list, dealer)
                break
        elif action.startswith("st"):
            print(f"{player.name} chooses to stand.")
            break
        elif action.startswith("sp"):
            print(f"{player.name} chooses to split hands.")
            handle_split(player, deck, hand, player_list, dealer)
            player_action(player, deck, hand, split_tolerance, player_list, dealer)
            break
        else:
            print("Invalid choice. Please enter 'split', 'double', 'hit', or 'stand'.")

def shs(player, deck, hand, split_tolerance, player_list, dealer):
    """Handle the player's decision to split, hit, or stand."""
    while True:
        hand.display_hand()
        action = input(f"{player.name}, would you like to split, hit, or stand? (Enter 'split', 'hit', or 'stand')").lower()
        if action.startswith("h"):
            handle_hit(player, deck, hand, player_list, dealer)
            break
        elif action.startswith("st"):
            print(f"{player.name} chooses to stand.")
            break
        elif action.startswith("sp"):
            print(f"{player.name} chooses to split hands.")
            handle_split(player, deck, hand, player_list, dealer)
            player_action(player, deck, hand, split_tolerance, player_list, dealer)
            break
        else:
            print("Invalid choice. Please enter 'split', 'hit', or 'stand'.")

def hs(player, deck, hand, player_list, dealer):
    """Handle the player's decision to hit or stand round."""
    while True:
        hand.display_hand()
        action = input(f"{player.name}, would you like to hit, or stand? (Enter 'hit' or 'stand')").lower()
        if action.startswith("h"):
            handle_hit(player, deck, hand, player_list, dealer)
            break
        elif action.startswith("s"):
            print(f"{player.name} chooses to stand.")
            break
        else:
            print("Invalid choice. Please enter 'hit' or 'stand'.")

def evaluation(player,hand,dealer_hand):
    if hand.hand_value > 21:
        player.lose()
        print(f"{player.name} bust this round Hand Value:({hand.hand_value}) Player Loses:{player.bet} Player Balance:{player.balance}")
    elif hand.hand_value == 21 and dealer_hand.hand_value != 21:
        player.win()
        print(f"{player.name} hit Blackjack! Hand Value:({hand.hand_value}) Player Wins:{player.bet} Player Balance:{player.balance}")
    elif hand.hand_value == dealer_hand.hand_value:
        if hand.hand_value == 21:
            player.win()
            print(f"{player.name} hit Blackjack! Hand Value:({hand.hand_value}) Player Wins:{player.bet} Player Balance:{player.balance}")
        else:
            print(f"{player.name} has pushed Hand Value:({hand.hand_value}) Player Wins:0.0 Player Balance:{player.balance}")
    elif hand.hand_value > dealer_hand.hand_value:
        player.win()
        print(f"{player.name} wins Hand Value:({hand.hand_value}) Player Wins:{player.bet} Player Balance:{player.balance}")
    elif hand.hand_value < dealer_hand.hand_value:
        if dealer_hand.hand_value > 21:
            player.win()
            print(f"The dealer has bust, {player.name} wins Hand Value:({hand.hand_value}) Player Wins:{player.bet} Player Balance:{player.balance}")
        else:
            player.lose()
            print(f"{player.name} loses Hand Value:({hand.hand_value}) Player Loses:{player.bet} Player Balance:{player.balance}")