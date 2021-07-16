import keyboard
from coffee_recipes import MENU


# setting up the quantity of ingredients
resources = {
    "water": 1000,
    "milk": 1000,
    "coffee": 1000,
    "money" : 0
}


# function to check if there are enough ingredients for the coffee requested
def check_resources(coffee_name):

    sufficient = True

    if resources['water'] < MENU[coffee_name]['ingredients']['water']:
        sufficient = False
        print("Not enough water...")
    
    if resources['milk'] < MENU[coffee_name]['ingredients']['milk']:
        sufficient = False
        print("Not enough milk")
    
    if resources['coffee'] < MENU[coffee_name]['ingredients']['coffee']:
        sufficient = False
        print("Not enough coffee powder")

    return sufficient


# function to get the coins(cash) for the coffee. 
def get_coins(coin_name):
    while True:
        coins = input(f"How many {coin_name}? :").strip()
        if coins.isnumeric():
            coins = int(coins)
            if coins >= 0:
                return coins
            else:
                print("You can't enter a negative number")
        else:
            print("Invalid amount. Please enter again")


# function to check if the coins given by user are sufficient for the coffee requested. 
# for each coin value, the get_coins function is called. 
def check_money(coffee_name):
    price = MENU[coffee_name]['cost']
    print(f"Your coffee costs ${price}. Please insert the coins.")
    quarters = get_coins("quarters")
    dimes = get_coins("dimes")
    nickels = get_coins("nickels")
    pennies = get_coins("pennies")

    cash = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)

    if cash < price:
        print("Insufficient amount. Coins refunded.")
        return False
    elif cash > price:
        print(f"Here's your ${round(cash - price,2)} back.")
        return True
    else:
        print("Thanks for providing exact change!")
        return True


# function that will reduce the ingredients for the coffee made. And also to add the money 
def make_coffee(coffee_name):
    resources['water'] -= MENU[coffee_name]['ingredients']['water']
    resources['milk'] -= MENU[coffee_name]['ingredients']['milk']
    resources['coffee'] -= MENU[coffee_name]['ingredients']['coffee']
    resources['money'] += MENU[coffee_name]['cost']


# function to validate the user input. 
def get_input():

    valid_inputs = ['latte','espresso','cappuccino','report','off','restock']
    while True:
        user_input = input("Enter your coffee choice (latte/ espresso/ cappuccino): ").strip().lower()
        if user_input in valid_inputs:
            return user_input
        else:
            print("Invalid input, please try again")


# main body of the function.
# in addition to the coffee types, 3 commands report, restock, and off are available for admin
# prompts the user for input,
# if its a coffee type, checks if there's enough ingredients and user gave enough cash, and then makes coffee
# if input is one of the admin commands, then performs the respective actions.
# these admin commands are not shown in the prompt to the user. 

while True:

    coffee = get_input()

    if coffee == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")

    elif coffee == 'restock':
        resources['water'] = 1000
        resources['milk'] = 1000
        resources['coffee'] = 1000
        print("Ingredients restocked")

    elif coffee == 'off':
        print("\nPress escape to confirm exit.")
        keyboard.wait('esc')
        exit()

    else:
        if check_resources(coffee):
            if check_money(coffee):
                make_coffee(coffee)
                print(f"Please enjoy your ☕ {coffee}")
            
        else:
            print("Not enough ingredients, please contact owner")

