from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# This is a OOP version of the coffee machine code from Day 15. 
# The classes and methods were provided as starter code. 
# Only thing I changed was the resource amount to 1000 each

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_is_on = True

while machine_is_on:

    # get the input from user
    choice = input("Enter your input option : latte/espresso/cappuccino :").strip().lower()

    # if input is report, then print the report. if off, then exit the program
    # if its something else, check if its a coffee type offered, and if yes, check ingredients and payment
    # if not, then display error message
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        machine_is_on = False
    else:
        coffee = menu.find_drink(choice)
        if coffee != None:
            if coffee_maker.is_resource_sufficient(coffee):
                if money_machine.make_payment(coffee.cost):
                    print("Ready to give you your coffee")
                    coffee_maker.make_coffee(coffee)
            else:
                print("We regret the incovenience caused...")

        


