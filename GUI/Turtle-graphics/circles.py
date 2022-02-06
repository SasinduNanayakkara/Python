# import packages
import random
import turtle
from random import Random
from turtle import Turtle, Screen

# create objects
tim = Turtle()

# change colormode
turtle.colormode(255)

tim.pensize(5)
# speed up
tim.speed("fastest")

# generate random color (r g b)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

# draw the spirograph
def draw_spirograph(gap):
    for i in range(int(360 / gap)):
        tim.color(random_color()) # change the color randomly
        tim.circle(150) # draw a circle
        tim.setheading(tim.heading() + gap) # change the position


draw_spirograph(10) # call the function to draw the spirograph

screen = Screen()
screen.exitonclick()