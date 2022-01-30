# import classes and packages
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# setup the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # stop the screen updating
# create objects
player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up") # program the keyboard to move the turtle

game_is_on = True
while game_is_on:  # start the game
    time.sleep(0.1)
    screen.update() # update the screen

    carManager.create_car() # create a new car
    carManager.move_cars()  # move the car

    # detect the collusion with car
    for car in carManager.all_cars:
        if car.distance(player) < 30: # check the distance between turtle and car
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if player.is_at_finish_line(): # when turtle come to the finish line
        player.go_to_start()
        carManager.level_up()
        scoreboard.increase_the_level()




screen.exitonclick()