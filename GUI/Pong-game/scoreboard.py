# import packages
from turtle import Turtle
# create a class inherited with Turtle class
class Scoreboard(Turtle):

    def __init__(self): # constructor
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    # update the score boards
    def update_scoreboard(self):
        self.clear()
        self.goto(-108, 200) # set the score board position
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # increase the left score
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    # increase the right score
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()



