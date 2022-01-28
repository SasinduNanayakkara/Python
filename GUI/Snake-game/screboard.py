# Scoreboard class
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Score(Turtle):

    def __init__(self): # constructor
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle() # disappear the turtle icon
        self.update_scoreboard()

    # update the scoreboard when snake eat a food
    def update_scoreboard(self):
        with open("data.txt") as file:
            self.high_score = file.read()
        self.write(f"score : {self.score}  High score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        self.score = 0

        with open("data.txt", "w") as file:
            file.write(str(self.high_score))

    # display the game over message
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    # increase the score
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
