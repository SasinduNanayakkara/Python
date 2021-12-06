def turnRight():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turnRight()
    move()
    turnRight()
    move()
 
while not at_goal():
    if front_is_clear() and not right_is_clear():
        move()
    else:
        if right_is_clear():
            jump()
        else:
            turn_left()
            