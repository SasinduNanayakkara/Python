# import packages
import random
from turtle import Turtle, Screen
from random import Random
tim = Turtle() # create object
colors = ["firebrick", "green yellow", "coral", "yellow", "medium violet red"]  # color list

# draw the shape
def draw_shape(num_sides):
    angle = 360 / num_sides  # change angle of the shape

    for i in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_sides in range(3, 11):
    tim.color(random.choice(colors)) # change color
    draw_shape(shape_sides) # draw the shape


screen = Screen()
screen.exitonclick()
