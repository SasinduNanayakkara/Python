# import packages
from turtle import Turtle

# create a class inherited with Turtle
class Ball(Turtle):

    def __init__(self): # constructor
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # move the ball
    def move(self):

        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    # bounce the ball to y positions
    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    # bounce the ball to x positions
    def bounce_x(self):
        self.x_move *= -1

    # reset the ball position
    def reset_the_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()



