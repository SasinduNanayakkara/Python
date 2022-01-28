# import classes and packages
from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from screboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # set the background color as black
screen.title("The Snake Game") # set a title
starting_position = [(0, 0), (-20, 0), (-40, 0)] # set the starting position of the segments(snake)
segments =[]
screen.tracer(0)  # stop the graphics

# create objects
snake = Snake()
food = Food()
score = Score()
screen.listen()

# add buttons events
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Right, "Right")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collusion with food
    if snake.head.distance(food) < 15:  # if snake pass the food
        food.refresh()
        snake.extends()
        score.increase_score()

    # if snake hit the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # game_is_on = False
        # score.game_over()
        score.reset()
        snake.reset()

    for segments in snake.segments[1:]:

        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:  # when snake hit its tail
            # game_is_on = False
            # score.game_over()
            score.reset()
            snake.reset()


screen.exitonclick()
