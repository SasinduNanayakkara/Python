logoReeborg's World

Maze ✓🤖
 World Info 
Python
 Reeborg's keyboard Additional options
English
 

reverse step run step pause stop reload 
 138/138   
Python CodelibraryA↑AA↓A
def turnRight():
    turn_left()
    turn_left()
    turn_left()
​
while front_is_clear():#fixed the bug with infinite loop
    move()
turn_left()
    
​
​
while not at_goal():
    if right_is_clear():
        turnRight()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
Basic commands
Defining
Loops
Decisions
Conditions
Using variables