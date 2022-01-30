# import package
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

# create a class inherited with the Turtle class
class Player(Turtle):

    def __init__(self): # constructor
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    # move the turtle
    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    # check if turtle came to the finish line
    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    # go back to the start position
    def go_to_start(self):
        self.goto(STARTING_POSITION)