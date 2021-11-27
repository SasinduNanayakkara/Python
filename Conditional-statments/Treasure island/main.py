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


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
direction = input('You\'re at a crossroad, where do you want to go? Type "left" or "right". :').lower()

if direction == "right":
  print("fall into a hole.\nGame over")

elif direction == "left":
  work = input("You have come to a lake. There is an island in the middle of the lake type 'wait' for wait for a boat or type 'swim' to swim across :").lower()

  if work == "swim" :
    print("Attacked by trout.\nGame Over")
  elif work == "wait":
    door = input('You arrived at the island unharmed. There is a house with 3 doors. One red, One yellow and one blue. Which color do you choose ? : ').lower()
    
    if door == "red":
      print("Burned by fire.\ngame over")
    elif door == "blue":
      print("Eaten by beasts.\nGame Over.")
    elif door == "yellow":
      print("You Win!!!\n You got the treasure")
    else:
      print("Wrong command typed \n Game Over")
  else:
    print("Wrong command typed \n Game Over")

else:
  print("Wrong command typed \n Game Over")