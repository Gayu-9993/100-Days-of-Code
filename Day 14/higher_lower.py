from game_data import data
from art import logo,vs
import random 
from os import system, name
import keyboard

# This is a game of higher - lower. You will be have two options of famous personalities and business entities
# You will have to guess which one of them has the most number of followers on Instagram. 
# You can play multiple games, and the highscrore is tracked for each session of gaming. 


# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# define a function to get the second option and compare it with first one so its not the same 
def get_option_B(opt_A):

    opt_B = random.choice(data)

    while data.index(opt_B) == data.index(opt_A):

        opt_B = random.choice(data)
    
    return opt_B

# a function to keep pestering the user for a valid input. 
# using parameters to use same function for choosing option A/B and for the Yes or No questions

def get_input(opt1,opt2):
    
    while True:

        inp = input().strip().upper()[0]

        if inp == opt1 or inp == opt2:
            return inp
        else:
            print("Please enter a valid character")

# Main function of the program, that holds the loop for the gameplay, and returns the user's score when game over
def play_game():

    points = 0
    game_over = False

    option_A = random.choice(data)
    option_B = get_option_B(option_A)

    while not game_over:
        clear()

        print(logo)

        print(f"\n\nYou've got {points} points")

        print(f"Option A : {option_A['name']}, a {option_A['description']} from {option_A['country']}")

        print(vs)

        print(f"Option B : {option_B['name']}, a {option_B['description']} from {option_B['country']}\n\n")

        print("Who has the greater number of followers? A or B : ",end='')
        user_input = get_input('A','B')

        ### check which option has more followers and which option the user gave. 

        if user_input == 'A': 
            if option_A['follower_count'] >= option_B['follower_count']:
                points += 1
                option_B = get_option_B(option_A)
            else:
                print("You lose")
                game_over = True

        elif user_input == 'B':
            if option_B['follower_count'] >= option_A['follower_count']:
                points += 1
                option_A = option_B
                option_B  = get_option_B(option_A)
            else:
                print("You lose")
                game_over = True


    return points


highscore = 0
score = 0
game = True

print(logo)

print("\n\nWould you like to play a game? Y or N")

### usng a loop here to get multiple games. 
### also keeping track of the scores to display a highscore at the end. 
while game:   

    choice = get_input('Y','N')
    if choice == 'Y':
        score = play_game()
        if highscore == 0 and score != 0:
            highscore = score
            print("you're score is ",score)
            print("You've set the highscore")
        elif score >= highscore and highscore != 0:
            highscore = score
            print("your score is ",score)
            print("You got the high score..!!!")
        else:
            print("your score is ",score)
            print("highscore is ",highscore)
        
        print("\n\nWould you like to play another game ? Y or N")

    else:
        print("\nOkay then. Goodbye!")
        game = False

### using keyboard.wait() to wait until escape key is pressed. 
print("\nPress escape to exit")
keyboard.wait('esc')