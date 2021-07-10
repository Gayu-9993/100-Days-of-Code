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

def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

operator_dict = {'+':add,'-':subtract,'*':multiply,'/':divide}

def validate_input():
    while True:
        number = input().strip()
        if number.isnumeric():
            return int(number)
        else:
            print("Invalid input...Please enter a valid number : ")
    
def validate_operator():
    while True:
        operator = input().strip()[0]
        if operator in operator_dict:
            return operator
        else:
            print("Invalid operator selected. Please reenter : ")

def get_num1():
    global num1
    clear()
    print(logo)
    print("Enter your first number : ")
    num1 = validate_input()
    
get_num1()
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
