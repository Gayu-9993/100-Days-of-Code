from art import logo
import keyboard
import random
from os import system, name


### This is the code for a game of blackjack
### please refer the README.md file for a more detailed explanation of the rules. 

# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

### function to deal a card 
def dealcard():
    card = random.choice(cards)
    return card

### this is the main function for the gameplay. It returns the results of the game 
def play_game():
    for _ in range(2):
        user_cards.append(dealcard())
        dealer_cards.append(dealcard())
    
    ### Checking for a blackjack (cards total to 21)
    if sum(user_cards) == 21:
        if sum(dealer_cards) == 21:
            return "\nBoth got a blackjack, so its a draw"
        else:
            return "\nUser won with a black jack"
    elif sum(dealer_cards) == 21:
        return "\nDealer won with a blackjack"
    else:
        print("user cards are ",user_cards)
        print("Dealer's first card is ",dealer_cards[0])

    ### user gets to draw additional cards if their total is less than 21
    choice = input("Do you wish to choose your next card? Y or N : ").strip().upper()[0]
    while choice == 'Y':
        print("\nYou get a new card...")
        user_cards.append(dealcard())
        if sum(user_cards) > 21:

            ### if user total > 21, then if there's an ace in their hand, it is counted as 1 instead of 11
            if 11 in user_cards:
                user_cards.remove(11)
                user_cards.append(1)
                print("\nAdjusting the value of ace as your previous sum exceeded 21")
                print("user cards are ",user_cards)
                choice = 'N'
            else:
                print("user cards are ",user_cards)
                return "\nDealer won as user crossed 21"
        else:
            print("user cards are ",user_cards)
            choice = input("\nDo you wish to choose your next card? Y or N : ").strip().upper()[0]

    ### dealer will also choose new cards as long as the existing total is less than 17. 
    while sum(dealer_cards) < 17:
        print("\nDealer got a new card")
        dealer_cards.append(dealcard())
        if sum(dealer_cards) > 21:

            ### same reason as user. if ace in hand and total > 21, ace is counted as 1
            if 11 in user_cards:
                dealer_cards.remove(11)
                dealer_cards.append(1)
                break
            else:
                return "\nUser won as dealer crossed 21"

    print("\nUser cards are : ",user_cards)
    print("\nDealer cards are : ",dealer_cards)

    ### if both dont have blackjack and both totals are below 21, then the one with higher score wins.

    if sum(user_cards) == sum(dealer_cards):
        return "\nIts a draw match"
    elif sum(user_cards) > sum(dealer_cards):
        return "\nUser won..."
    elif sum(user_cards) < sum(dealer_cards):
        return "\nDealer won..."


### this will be the loop for the user to play multiple games. 
while input("\nDo you want to play a game of blackjack? Y or N : ").strip().upper()[0] == 'Y':
    clear()
    print(logo)
    user_cards = []
    dealer_cards = []
    print(play_game())

print("\nPress escape to exit")
keyboard.wait('esc')
