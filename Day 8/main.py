### This is a simple program that uses caesar cipher logic to encrypt and decrypt a string. 
### It prompts the user to choose either to encode or decode the string, the string itself and the key
### It then shifts the alphabets by the key value given, keeping the numbers and other special characters same 
### This program can be made to run in an infinite loop should the user choose to.

# import system and name from os to clear the terminal after one run
from os import system, name

  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# defining the list with all the alphabets - only lower case ones as we format input using lower()
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# ascii art for user satisfaction
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP``````  `"Y8ba,   ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   

                                 
           88             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

## define the function that performs the encoding and decoding

def cipher(text,shift,direction):
    new_word = ''
    
    # if option chosen is decode , then reverse the direction of the shift
    if direction == 'decode':
        shift *= -1
    
    # check if the character is in the alphabet list. If not, then keep the original character
    for character in text:

        # get the current index of the character and shift it based on user input
        if character in alphabet:
            in_place = alphabet.index(character)

            new_place = in_place + shift

            if new_place > (len(alphabet) - 1):
                new_place = new_place - len(alphabet) 

            new_word += alphabet[new_place]
        else:
            new_word += character

    return new_word

# define function to validate the user input. 
# 2 use cases - one to check encode/decode option and other to check user input is 'y' or 'n' for continue
def validate_input(option1,option2):
    while True: 
        user_input = input().lower().strip()
        if user_input == option1 or user_input == option2:
            return user_input
        else:
            print("Please enter a valid entry")

# keeping the main part of the program in an infinite loop to facilitate multiple uses
#          
while True:
    print(logo)

    # get the cipher option, input string and the shift key value

    print("\n\nType 'encode' to encrypt, type 'decode' to decrypt: ")
    direction = validate_input('encode','decode')
    text = input("Type your message:\n").lower().strip()
    shift = int(input("Type the shift number:\n"))
    shift = shift%26  # this is incase the shift value exceeds the number of alphabets. 
    cipher_word = cipher(text,shift,direction)
    print(f"Here's the {direction}d result : ",cipher_word) # display the output
    
    # prompt the user to chose to repeat the process or exit
    print("Do you wish to continue ? Y or N : ")
    cont = validate_input('y','n')
    if cont == 'n':
        print("Thank you for using our services. Have a great day")
        break
    else:
        clear()
    
