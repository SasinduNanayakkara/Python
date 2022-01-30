# import packages
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

# create class
class CarManager(Turtle):
    def __init__(self):  # constructor
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # create random car
    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1: # when random number become 1 create a car

            new_car = Turtle("square") # create object
            new_car.shapesize(stretch_len=2, stretch_wid=1) # resize the turtle object as car
            new_car.penup()
            new_car.color(random.choice(COLORS))  # pick a color as random
            random_y = random.randint(-250, 250)  # select car starting position randomly
            new_car.goto(300, random_y)
            self.all_cars.append(new_car) # add to the car list
    # move the car
    def move_cars(self):
        for cars in self.all_cars:
            cars.backward(self.car_speed)

    # increase the car moving speed
    def level_up(self):
        self.car_speed += MOVE_INCREMENT




