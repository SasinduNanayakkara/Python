from turtle import Turtle, Screen

tim = Turtle()  # creating objects
screen = Screen()

# move forward the turtle
def move_forward():
    tim.forward(10)

# go backward the turtle
def move_backward():
    tim.backward(10)

# turn left
def turn_left():
    tim.left(10)

# turn right
def turn_right():
    tim.right(10)
# clear the display
def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen() # event listning
screen.onkey(key="w", fun=move_forward) # when press w call the move_forward function and move forward
screen.onkey(key="s", fun=move_backward) # when press s call the move_backward function and move backward
screen.onkey(key="a", fun=turn_left) # when press a call the turn_left function and turn left
screen.onkey(key="d", fun=turn_right)  # when press d call the turn_right function and move turn right
screen.onkey(key="c", fun=clear) # when press c call the clear function and clear the screen

screen.exitonclick()