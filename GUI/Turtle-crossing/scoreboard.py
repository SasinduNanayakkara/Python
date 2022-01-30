# import packages
from turtle import Turtle
FONT = ("Courier", 24, "normal")

# create a class inherited with Turtle class
class Scoreboard(Turtle):
    def __init__(self): # constructor
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 1
        self.update_score_board()

    # update the score board and print the level
    def update_score_board(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level : {self.score}", align="left", font=FONT)

    # increase the level number
    def increase_the_level(self):
        self.score += 1
        self.update_score_board()

    # Display the game over at the center of the screen
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

