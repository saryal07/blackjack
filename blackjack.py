# Use randint to generate random cards.
from blackjack_helper import *

def get_player_count():
    while True:
        try:
            count = input("Welcome to Blackjack! How many players? ")
            count = int(count)
            if count > 0:
                return count
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Main program starts here
player_count = get_player_count()
player_names = []

for i in range(player_count):
    player_name = input(f"What is player {i + 1}'s name? ")
    player_names.append(player_name)

# Function to handle a player's turn
def player_turn(player_name):
    user_hand = draw_starting_hand(player_name.upper())
    while user_hand < 21:
        should_hit = input(f"You have {user_hand}. Hit (y/n)? ").lower()
        if should_hit == 'n':
            break
        elif should_hit != 'y':
            print("Sorry I didn't get that.")
        else:
            user_hand = user_hand + draw_card()
    print_end_turn_status(user_hand)
    return user_hand

# Function to handle the dealer's turn
def dealer_turn():
    dealer_hand = draw_starting_hand("DEALER")
    while dealer_hand < 17:
        print(f"Dealer has {dealer_hand}.")
        dealer_hand = dealer_hand + draw_card()
    print_end_turn_status(dealer_hand)
    return dealer_hand

# PLAYER'S TURN
for player_name in player_names:
    user_hand = player_turn(player_name)

    # DEALER'S TURN
    dealer_hand = dealer_turn()

    # GAME RESULT
    print_end_game_status(user_hand, dealer_hand)