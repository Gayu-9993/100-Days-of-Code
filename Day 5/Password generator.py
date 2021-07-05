import random
import keyboard

# import random to use the choice and sample methods 

# defining the list of alphabets, numbers and symbols allowed

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


### using the function call to loop until a valid number is received for all 3 inputs
def user_input():
    while True:
        your_choice = input().strip()
        if your_choice.isnumeric():
            your_choice = int(your_choice)
            return your_choice
        else:
            print('Invalid Input Character.Please enter again.')

print("Welcome to the PyPassword Generator!\n\n")
print("How many letters would you like in your password?")

### Need to check if the total charactes wanted is more than 0. 
total_letters= user_input()
while True:
    if total_letters <= 0 :
        print("Please enter a number greater than 0")
        total_letters= user_input()
    else:
        break

# Once we get the characters count, ask for the number of symbols and make sure they dont exceed the characters requested
# Not checking for 0 as we might need a password with no symbols

print("How many symbols would you like?")
num_symbols = user_input()
while True:
    if num_symbols > total_letters:
        print(f"Enter a number less than {total_letters}")
        num_symbols = user_input()
    else:
        break

# Similar to symbols, but checking if the symbols count == total chars 
# if yes, then automatically setting the count of numbers to 0 as we dont have any space for them 

if total_letters - num_symbols != 0:
    print("How many numbers would you like?")
    num_numbers = user_input()
    while True:
        if num_numbers > (total_letters - num_symbols):
            print(f"Enter a number less than {total_letters - num_symbols}")
            num_numbers = user_input()
        else:
            break
else:
    num_numbers = 0

# Getting the count of just the alphabets
num_letters = total_letters - num_symbols - num_numbers

# using the random.choice to pull characters from the lists for each category
password = ''
for char in range(num_letters):
    letter = random.choice(letters)
    password += letter

for num in range(num_numbers):
    number = random.choice(numbers)
    password += number

for sym in range(num_symbols):
    symbol = random.choice(symbols)
    password += symbol

# using the sample and join methods to shuffle the order of the characters within the password
random_password = random.sample(password,total_letters)
password = ''.join(random_password)

# Finally, output to be displayed on the screen. 
print("Our suggestion for your new Password is : ",password)

# Since I intend to make this as an exe as well, using wait() function
print("\n\nPlease press escape to exit")
keyboard.wait('esc')
