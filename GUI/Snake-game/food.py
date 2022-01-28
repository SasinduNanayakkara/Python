from turtle import Turtle, Screen
import random

# food class
class Food(Turtle):

    def __init__(self): # constructor
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5) # define the food size
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    # refresh the position of the food
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

