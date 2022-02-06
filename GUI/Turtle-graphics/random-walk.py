# import packages
import random
import turtle
from turtle import Turtle, Screen
from random import Random
# create an object
tim = Turtle()
# change colormode
turtle.colormode(255)

# generate random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)


# colors = ["firebrick", "green yellow", "coral", "yellow", "medium violet red"]
# turning angle list
direction = [0, 90, 180, 270]
tim.pensize(15) # change width of the drawing
tim.speed("fastest") # speed up
tim = Turtle() # create the object

for _ in range(200):
    tim.color(random_color()) # generate random color
    tim.forward(30)
    tim.setheading(random.choice(direction)) # change the direction randomly

screen = Screen()
screen.exitonclick()
