def turnRight():
    turn_left()
    turn_left()
    turn_left()

def passTheWall():
    
    turn_left()
    move()
    turnRight()
    move()
    turnRight()
    move()
    turn_left()
    


while not at_goal():
    if front_is_clear():
        move()
    else:
        passTheWall()
