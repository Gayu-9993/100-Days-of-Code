import random

### so, here goes my explanation for the deviation of the base logic used to perform the same thing as course solution

### I wanted the output to include the name of the choice I've made and not just the ASCII image. 
### therefore I had to resort to using dictionaries to fetch the names for each choice

### The reason I gave the ASCII images inside dictionaries as well was so I could play with 1,2,3 
### which is a bit easier than looking on the other end of the strip for 0. 

### and technically, Dictionaries are faster than Lists right, so OPTIMIZATION....  :-)


RPS_image = {
    'rock' : '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
,
'paper' : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
,
'scissors' : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}

RPS_dict = {1:'rock',2:'paper',3:'scissors'}

print("Welcome to the land of RPS...!!!")

print("\nLet's Begin")

continuous_gameplay = 'Y'
while continuous_gameplay == 'Y':
        
    while True: 
        choice = input("\n What do you choose? Type 1 for Rock, 2 for Paper and 3 for Scissors. Remember, numbers only please!")

        if choice.isnumeric():
            choice = int(choice)
            if choice >= 1 and choice <=3 : 
                break
            else:
                print("Please enter a valid response")
        else:
            print('characters detected. Please give a valid option')

    computer = random.randint(1,3) 

    print(f" You chose {RPS_dict[choice]}\n\n",RPS_image[RPS_dict[choice]])

    print(f"computer chose {RPS_dict[computer]}\n\n",RPS_image[RPS_dict[computer]])

    if choice == computer:
        print("It's a Draw")
    elif choice == 1 :
        if computer == 3:
            print('You win')
        else:
            print('You lose')
    elif choice == 2:
        if computer == 1:
            print('You win')
        else:
            print('You lose')
    elif choice == 3:
        if computer == 2:
            print('You win')
        else:
            print('You lose')   

    continuous_gameplay = input("Would you like another game ? Y or N... ").upper().strip()

print("Thanks for playing the Game...Good bye! ")
