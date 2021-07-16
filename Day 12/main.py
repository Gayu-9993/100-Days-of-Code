import random
import keyboard
from art import logo

random_number = random.randint(1,100)

print(logo)
print("\n\nwelcome to the game of Guess The number\n")
difficulty = input("PLease choose a difficulty : easy or hard ? ").strip().lower()

if difficulty == 'easy':
    lives = 10
elif difficulty == 'hard':
    lives = 5
else:
    print("invalid input. We'll go with easy mode for you...")
    lives = 10

print("I have choosen a number between 1 and 100..Take a guess...")


gameover = False
while not gameover:
    print(f"You have {lives} lives left.")
    guess = input("Please enter a number : ").strip()
    if guess.isnumeric():
        guess = int(guess)
        if guess < 1 or guess > 100:
            print("Choose a number between 1 and 100")
            lives -= 1
        else:
            if guess == random_number:
                print("\n~~ Yep, thats the one ~~")
                print("\n~~   Congratulations  ~~")
                gameover = True
            elif guess > random_number:
                print("nope, your guess is bigger than my number...")
                lives -= 1
            else:
                print("nope, your number is smaller than mine...")
                lives -= 1

            if abs(guess - random_number) < 5 and abs(guess - random_number) != 0:
                print("but you're too damn close")
    else:
        print("Invalid entry...you still lose a life.")
        lives -= 1

    if lives == 0:
        print("\n\nI'm sure you would have got it, but too bad you're out of lives.\n\nAdios Amigo")
        gameover= True

print("\nPress 'escape' to exit")
keyboard.wait('esc')
        
            
