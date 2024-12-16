print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("You're at a cross road. Where do you want to go?")
direction = input("Type 'Left' or 'Right' \n")

if direction == "Right":
    print("Fall into a hole. \n Game Over.")
if direction == "Left":
    print("You've come to a lake. There is an island in the middle of the lake with a plaque titled 'Welcome to the treasured island'")
    Decide_what_2_do = input("Decide! Type 'Wait' to wait for boat or type 'Swim' to swim across. \n")
    if Decide_what_2_do == "Swim":
        print("Attacked by trout. \n Game Over.")
    elif Decide_what_2_do == "Wait":
        print("You've arrived unharmed to the island and ready to hunt. There is a house with three doors of different colors in your front.")
        colour = input ("One Red, one Blue, and one Yellow. Which color do you choose to open? \n")
        if colour == "Yellow":
            print("You Win!")
        if colour == "Blue":
            print("Eaten by beasts.\nGame Over.")
        elif colour == "Red":
            print("Burned by fire.\nGame Over.")
        else:
            print("Game Over")

    else:
        print("Attacked by lions.\nGame Over.")
else:
    print("Try again and choose the right direction.\nGame Over.")





