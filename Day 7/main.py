import random

from wordlist import word_list
from artwork import stages

import keyboard
# import only system from os
from os import system, name
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def hangman():
    print('''
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/             
    ''')
    print("    Welcome to the land where we hang people for fun.\n")



word_choice = random.randint(0,len(word_list))

word_asked = word_list[word_choice]

print(f"btw, the answer is {word_asked}")

blank = [' ']
for letter in word_asked:
    blank.append('_ ')

user_inputs = []
lives_left = 6
blank_count = 0
hangman()

while lives_left > 0 : 

    print(stages[lives_left])
    print("Please try to guess the word:")
    print(''.join(blank))

    user_letter = input("give me a character : ").strip().lower()[0]

    clear()
     
    if user_letter in user_inputs:
        hangman()
        lives_left -= 1
        if lives_left != 0 : 
            print("God damn it man, you've already given that!!!")
            print(f"\nYou've got {lives_left} attempts left\n")
        
    elif user_letter in word_asked:
        positions = [pos for pos, char in enumerate(word_asked) if char == user_letter]
        for pos in positions: 
            blank[pos + 1] = user_letter
        hangman()
    else:
        hangman()
        lives_left -= 1
        if lives_left != 0:
            print('Unfortunately, we aint got that letter')
            print(f"\nYou've got {lives_left} attempts left\n")

    user_inputs += user_letter
    

    if "_ " in blank:
        if lives_left == 0:
            break
        else:
            print("The word is still missing something, and it definitely ain't love..")
    else:
        print(f"Well done. You managed to do it with {lives_left} lives left")
        print('''
                 ___________
                 \-=======-/
                _|   .=.   |_
               ((|  {{1}}  |))
                \|   /|\   |/
                 \__ '`' __/
                   _`) (`_
                 _/_______\_
                /___________\ ''')
        break

if lives_left == 0:
    print("You've exhausted all your lives.\n")
    print(stages[0])
    print("\nToo bad. A man can't even trust you to save his life...")
    print("\nBTW, the word was ",word_asked)


print("\n\npress escape to exit")
keyboard.wait('esc')
