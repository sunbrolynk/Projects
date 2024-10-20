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
direction = input("You come to a fork in the road, which direction do you choose, East, or West?\n")
if "West" != direction != "west":
    print("You are eaten by a dragon!")
    quit()
else:
    print("You Follow the path to the West")
canyon = input("You come to a valley with a small bridge across, and a winding path down, do you take The Bridge, or The Path\n")
if canyon == "The Bridge" or canyon == "the bridge" or canyon == "the Bridge" or canyon == "The bridge":
    print("You make it safely across the valley and continue on your journey!")
else:
    print("The path down the valley wall is riddled with snakes, your suffer a horrible death!")
    quit()
battle = input("You arrive at an arena with a warrior awaiting you, he offers you a choice of weapon: Sword, Staff, or Bow\n")
if battle == "Bow" or battle == "bow":
    print("You grab the bow and fire a shot through his head!\nYou live and gain the treasure!\nCongratulations!")
else:
    print("As your grab your weapon he lops off your head!\nYou are Dead.")