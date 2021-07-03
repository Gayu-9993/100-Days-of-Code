### this is a simple game of finding the treasure. You will be given a couple of scenarios

### you choose from the options given. Unless you type the correct option, you are dead

### Not much in the way of logic, but was definitely fun 

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
direction = input("Your path diverges. Which direction do you choose ? East or West ? ").lower().strip()

if direction != 'west':
    print("you dead bruh. Thats the path by the witch's house. She eats children for dessert")
else:
    print("You're walking the merry road humming a tune")
    for i in range(6):
        print("walking...")
    print("still walking...\n.\n.\n.\n.\n.\n.")
    print("You come to a River. You see no boat to cross with.")
    swimming = input("what do you do? swim or wait? ").lower().strip()
    if swimming != 'wait':
        print("Sorry, you were killed by Trouts..ahem..Piranhas")
    else:
        print("You wait until you see someone come by in a boat. you flag him down and he agrees to take you across.")
        print(".\n.\n.\n.\n.\n.\n.")
        print("You reach the other side of the river and you bid the good samaritan goodbye.")
        print(".\n.\n.\n.\nYou're walking the merry road humming a tune")
        print(".\n.\nYou see a cave and you enter it. This might be it. This might be the place you find the treasure. But sadly you got 3 doors to choose from.")
        door = input("Which door will you choose ? Red? blue? yellow? ").lower().strip()
        if door == 'red':
            print("oh no...it leads to a dragon's lair. You are now on the menu. You are also dead!!")
        elif door == 'blue':
            print("oh no...sea water gushed into the room flooding the cave,and with it came the sea serpent. You are one dead man.")
        elif door == 'yellow':
            print("Bless your damned soul, you actually found it....You found the lilliputian Treasure")
            print("GAME ENDS IN PEACE")
        else:
            print("You dead by your own stupidity....Learn to choose from the options")