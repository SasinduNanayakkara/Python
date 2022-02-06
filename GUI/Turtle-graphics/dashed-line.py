# import packages
from turtle import Turtle, Screen
# create an object
tim = Turtle()

for i in range(10):
    tim.forward(10)
    tim.penup() # keep a space
    tim.forward(10)
    tim.pendown() # again draw
    tim.forward(10)

screen = Screen()
screen.exitonclick()