############ DEBUGGING SNIPPETS OF CODE #####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

#### Debugged : range(1,20) will only go up to 19 as the upper limit is excluded

def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")


my_function()


# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

#### Debugged : index of list starts from 0. if we give a 6 for this list, we get a list index out of range 

from random import randint
from typing_extensions import TypeVarTuple
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0,5)
print(dice_imgs[dice_num])


# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

#### Debugged : You can either use a try-except statement if you want to display an error, but if a valid value is necessary, then loop it until you get a valid value

### Here's my version of the code

while True : 
    year = input("What's your year of birth?").strip()
    if year.isnumeric():
        year = int(year)
        break
    else:
        print("Invalid input, please enter a valid year")

if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

### Missing an else here as well, not sure if that's intentional. 


# # Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

#### Debugged : same case as above, either use try-except or use a loop till you get a correct input. 
#               also, need to convert the age to an integer
#               and also need to indent the print statement and make it an f-string tp use { }
while True:
    age = input("How old are you?")
    if age.isnumeric() and age > 0:
        age = int(age)
        break
    else:
        print("Please enter a valid age")

if age > 18: 
    print(f"You can drive at age {age}")
# missing an else here, not sure if that is intentional


# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

#### Debugged : the initialization of the variables with a value of 0 is not necessary
#               should use = instead of ==
#               also need  loop/try-except to check if the input is indeed a number. 

while True:
    pages = input("Number of pages: ")
    if pages.isnumeric():
        pages = int(pages)
        break
    else:
        print("Invalid number. please enter again")

while True:
    word_per_page = input("Number of words per page: ")
    if word_per_page.isnumeric():
        word_per_page = int(word_per_page)
        break
    else:
        print("Invalid number, please print again")

total_words = pages * word_per_page
print(total_words)


# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

#### Debugged : fixed the indentation 

def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)


mutate([1, 2, 3, 5, 8, 13])
