import sys

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

game_is_on = True

while game_is_on:

    direction = input("You find yourself at a crossroad, do you want to go left or right? choose l/r \n")

    if direction == 'l':
        island = input("You are now at a lake with a mysterious island in the center. Do you swim or wait for a boat? Choose s/w. \n")

    else:
        print("You fall into a hole. Game over!")
        break

    if island == 'w':
        print("You arrive safely at the island a come across a structure with three doors that are yellow, blue, and green. Choose y/b/g \n")
        door = input("Which door do you enter?")

    else:
        print("You were eaten by swarm of killer fish. Game over!")

    if door == 'b':
        print("Congratulations! You have found the treasure.")

    elif door == 'y':
        print("You fall onto a bed of spikes. Ouch! Game over.")

    elif door == 'g':
        print("You become engulfed in flames. An unfortunate ending! Game over.")

    else:
        print("That wasn't one of the choices. Game over!")

    restart = input("Do you want to restart? y/n")

    if restart == 'n':
        sys.exit()


