from art import logo
from os import system, name
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

### Define individual functions for each arithmetic option and call them via the dictionart

def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

operator_dict = {'+':add,'-':subtract,'*':multiply,'/':divide}


### Function to keep prompting the user until a valid number is entered. 
def validate_input():
    while True:
        number = input().strip()
        if number.isnumeric():
            return int(number)
        else:
            print("Invalid input...Please enter a valid number : ")


### Function to validate the operation symbol pressed by user is valid, and to keep asking until it is right     
def validate_operator():
    while True:
        operator = input().strip()[0]
        if operator in operator_dict:
            return operator
        else:
            print("Invalid operator selected. Please reenter : ")


### since we are having an option to use the previous result as an operand for the next calculation
### keeping the part to get the first number out of the main loop
def get_num1():
    global num1
    clear()
    print(logo)
    print("Enter your first number : ")
    num1 = validate_input()
    
get_num1()


### Main loop of the program. Choose the inputs and the operators to get the calculated result. 
### then choose if the next operation is to be performed on the result or a new pair of numbers

while True:
    print("Choose an operator : ",end='')
    print("'+':add,'-':subtract,'*':multiply,'/':divide")
    operator = validate_operator()
    num2 = validate_input()
    calculation = operator_dict[operator](num1,num2)
    print(f"result of {num1} {operator} {num2} is {calculation} ")

    choice = input("\n Do you wish to contine calculations on the result ? Y or N : ").strip().upper()[0]
    if choice == 'Y':
        num1 = calculation
    else:
        clear()
        get_num1()
