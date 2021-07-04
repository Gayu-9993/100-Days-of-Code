import random
import keyboard

### Initialize the values. Keeping score as -1 to start off
your_score = -1
computer_score = -1
Not_Out = True

your_choice = 0
computer_choice = 0

### This function runs in a loop until the user gives a valid response. 

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

### this function is called when the user is batting...Need to check the defend count as well for user. 

### Function ends when either user defends more than 3 times in a row or
### user is on the chase and scores more than the computer
### user takes a double century
### and obviously the computer bowls the same number as you

def batting():
    your_batting_score = 0
    defend_count = 0

    while True:
        print("Please enter a number between 1 and 6 to score and 0 to defend : ")
        your_runs = user_input(0,6)
        computer_runs = random.randint(1,6)
        print(f"Computer chose to bowl a {computer_runs}\n")  

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
            print("Your score is ",your_batting_score)
            return your_batting_score

        if your_batting_score >= 200:
            print("200 has been reached..Sayonara")
            return your_batting_score


### This function is called when the computer is batting

### Defend score is not checked here as the computer is fearless and doesnt defend itself
### The function ends when either the computer scores more than user or scores a double century 
### and obviously when user bowls the same number as the computer

def bowling():
    computer_batting_score = 0
    while True:
        print("Enter a number between 1 and 6 to bowl")
        your_runs = user_input(1,6)
        computer_runs = random.randint(1,6) 
        print(f"Computer chose to hit it for a {computer_runs}\n")  

        if computer_runs == your_runs:
            print("Computer is OUT! Computer's score is ",computer_batting_score)
            return computer_batting_score
        
        computer_batting_score += computer_runs 

        if computer_batting_score > your_score and your_score != -1:
            print("Computer's score is ",computer_batting_score)
            return computer_batting_score

        if computer_batting_score >= 200:
            print("Computer has scored a DOUBLE CENTURY and is retiring")
            return computer_batting_score


### Prompt user for either 1 or 2. 

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

### Based on the winner of the toss, decide who bats and who bowls first
### if user choses even and the combo is even, or both are odd, then user won the toss. 

if (odd_even == 2 and combo_odd_even%2 == 0) or (odd_even == 1 and combo_odd_even%2 == 1):
    print("You won the Toss...Choose : 1 for Batting and 2 for Bowling : ")
    your_choice = user_input(1,2)
    if your_choice == 1 : 
        print("\n\nYou are now at the crease\n")
        your_score = batting()
        print(f"\nComputer needs {your_score + 1} to win")
        print("\n\nComputer is now at the crease\n")
        computer_score = bowling()
    else:
        print("Computer is now at the crease")
        computer_score = bowling()
        print(f"You need {computer_score + 1} to win")
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
        print(f"\nComputer needs {your_score + 1} to win")
        print("\n\nComputer is now at the crease\n")
        computer_score = bowling()


### End of the odd or even loop. Now onto the scoring

### To display the celebratory message : 
### we dont ridicule people who scored nothing, so we dont check for 0.

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

### This was something new I learned especially for this ..!
### otherwise the exe version just closes without giving user time to read the final verdict

keyboard.wait('esc')