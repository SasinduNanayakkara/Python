# import packages
import random
import turtle

import colorgram
from turtle import Turtle, Screen
from random import Random
# colors = colorgram.extract('painting.jpg', 30)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]
# create object
tim = Turtle()
turtle.colormode(255)

# tim.dot(20)
# tim.penup()
# tim.forward(50)
# tim.pendown()
# tim.dot(20)
# tim.forward(50)
# tim.dot(20)

tim.speed("fastest")  # speed up
tim.penup() # keep space
tim.hideturtle() # hide the icon
# set the start position
tim.setheading(220)
tim.forward(300)
tim.setheading(0)

for i in range(10): # manage rows
    for _ in range(10): # manage columns
        # draw a dot and keep a space
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)
        tim.pendown()
    # set a new line
    tim.penup()
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


screen = Screen()
screen.exitonclick()