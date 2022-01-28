# import classes and packages
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create objects
screen = Screen()
screen.tracer(0)  # stop the screen updates
screen.setup(width=800, height=600) # setup the window size
screen.bgcolor("black")
screen.title("Pong") # add a title

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()  # create objects
scoreboard = Scoreboard()

screen.listen()

# program the keyboard keys to move the paddles
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on: # start the game

    screen.update() # update the screen
    time.sleep(ball.move_speed)  # control the speed of the ball
    ball.move() # move  the ball

    # detect the collusion
    if ball.ycor() > 280 or ball.ycor() < -280: # when the ball hit the right top corner
        ball.bounce_y()

    # detect the paddle collusion
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect right paddle misses
    if ball.xcor() > 390:
        ball.reset_the_position()
        scoreboard.l_point()


    # detect left paddle misses
    if ball.xcor() < -390:
        ball.reset_the_position()
        scoreboard.r_point()



screen.exitonclick()

