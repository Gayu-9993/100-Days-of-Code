import random
import keyboard

your_score = -1
computer_score = -1
Not_Out = True

your_choice = 0
computer_choice = 0



def user_input(lowerend,upperend):
    while True:
        your_choice = input().strip()
        if your_choice.isnumeric():
            your_choice = int(your_choice)
            if your_choice <lowerend or your_choice >upperend:
                print('Invalid Input Number.Please enter again.')
            else:
                return your_choice
        else:
            print('Invalid Input Character.Please enter again.')


def batting():
    your_batting_score = 0
    defend_count = 0

    while True:
        print("Please enter a number between 1 and 6 to score and 0 to defend : ")
        your_runs = user_input(0,6)
        computer_runs = random.randint(1,6)

        if your_runs == computer_runs:
            print('You are out...Your score is ',your_batting_score)
            return your_batting_score

        if your_runs == 0:
            defend_count += 1
        else:
            defend_count = 0

        if defend_count >= 3:
            print('You have defended 3 or more times. This isnt a test match, You are out...')
            return your_batting_score

        your_batting_score += your_runs

        if your_batting_score > computer_score and computer_score != -1: 
            return your_batting_score

        if your_batting_score >= 200:
            print("200 has been reached..Sayonara")
            return your_batting_score

def bowling():
    computer_batting_score = 0
    while True:
        print("Enter a number between 1 and 6 to bowl")
        your_runs = user_input(0,6)
        computer_runs = random.randint(1,6)   

        if computer_runs == your_runs:
            print("Computer is OUT! Computer's score is ",computer_batting_score)
            return computer_batting_score
        
        computer_batting_score += computer_runs 

        if computer_batting_score > your_score and your_score != -1:
            return computer_batting_score

        if computer_batting_score >= 200:
            print("Computer has scored a DOUBLE CENTURY and is retiring")
            return computer_batting_score




print("Time for the toss : Enter 1 for Odd and 2 for Even")
odd_even = user_input(1,2)
if odd_even == 1:
    print('You chose odd')
elif odd_even == 2:
    print('You chose even')
else: 
    print("Check the odd or even settings")

print("Now enter a number between 1 and 6")
your_choice = user_input(1,6)
computer_choice = random.randint(1,6)

combo_odd_even = your_choice + computer_choice 



if odd_even == 2 and combo_odd_even%2 == 0:
    print("Choose : 1 for Batting and 2 for Bowling : ")
    your_choice = user_input(1,2)
    if your_choice == 1 : 
        print("\n\nYou are now at the crease\n")
        your_score = batting()
        print(f"\nComputer needs{your_score + 1} to win")
        print("\n\nComputer is now at the crease\n")
        computer_score = bowling()
    else:
        print("Computer is now at the crease")
        computer_score = bowling()
        print("You are now at the crease.")
        your_score = batting()
else:
    computer_choice = random.randint(1,2)
    if computer_choice == 1 : 
        print("\n\nComputer won the toss and chose to Bat first\n")
        computer_score = bowling()
        print(f"You need {computer_score + 1} to win")
        print("\n\nYou are now at the crease\n")
        your_score = batting()
    else:
        print("\n\nComputer won the toss and chose to Bowl first\n")
        your_score = batting()
        print("\n\nComputer is now at the crease\n")
        computer_score = bowling()


### End of the odd or even loop. Now onto the scoring



if your_score >= 200:
    print("Thats a double century for you..take a bow!")
elif your_score >= 100:
    print("Thats a century for you..take a bow!")
elif your_score >= 50:
    print("Thats a half century for you..take a bow!")

if computer_score == your_score:
    print("\nOh my god! Its a tie...")
elif computer_score > your_score:
    print("\nToo Bad...you LOST!!!")
else:
    print("\nCongratulations ... You Won!")

print("Done...press escape to exit")

keyboard.wait('esc')