# import packages
from  turtle import Turtle
# create a class inherited with Turtle class
class Paddle(Turtle):

    def __init__(self, position): # constructor
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5) # set the paddle size
        self.penup()
        self.goto(position)

    # change the position of the paddle
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)