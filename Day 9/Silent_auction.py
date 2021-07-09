#This is program to mimic a silent auction
# Items will be chosen at random for every execution of this program
# The bidder has to enter their name and the amount they are willing to bid.
# Once the bidder has cleared the screen, there will be a prompt for the next bidder. 
# If there are none, then the N option can be chosen to close the bid and announce the results. 



import random
import keyboard

# import system from os to clear the terminal after one run
from os import system
  

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
auction = {}
def auction_bid(name,bid):
    auction[name] = bid

items_list = ["Superman's Undies","Spiderman's Webslinger","Batmobile","The Gauntlet of Thanos","Lasso of Hestia","Replica of Thor's Hammer","Mark V IronMan Suit","Captain America Trading Cards"]

item_on_display = random.choice(items_list)

def starter():
    _ = system('cls')
    print(logo)
    print("\nWelcome to the Secret Auction\n")
    print(f"Today, we have here on display : {item_on_display}")

continue_auction = 'y'

while continue_auction == 'y':
    starter()
    print("\nPlease present the details of your bid below : \n")
    name = input("What is your name? - ").strip().capitalize()
    bid = int(input("How much are you willing to bid for? $"))
    auction_bid(name,bid)
    print("Thank you for your time. Your bid has been added to our list. Please await results")
    print("Press Escape to clear the screen")
    keyboard.wait('esc')
    starter()
    continue_auction = input("Are there anyone wishing to bid? Y or N ").strip().lower()[0]

highest_bid = 0

for bidder in auction:
    if auction[bidder] > highest_bid:
        highest_bid =auction[bidder]
        highest_bidder = bidder

print(f"\nThe highest bidder is {highest_bidder} with a bidding amount of ${highest_bid}")

