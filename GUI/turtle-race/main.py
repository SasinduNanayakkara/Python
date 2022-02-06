import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()  # create screen objects
screen.setup(width=500, height=400)   # set up width and height of the window
# create prompts ti get user input
user_bet = screen.textinput(title="make your bit", prompt="Which turtle will win the race? enter a color : ")
colors = ["red", "green", "blue", "yellow", "purple", "orange"]
y_position = [-150, -100, -50, 0, 50, 100] # turtles positions
turtles = []


# tim = Turtle(shape="turtle")
# tim.color(colors[0])
# tim.penup()
# tim.goto(x=-230, y=-150)
#
# tim1 = Turtle(shape="turtle")
# tim1.color(colors[1])
# tim1.penup()
# tim1.goto(x=-230, y=-100)
#
# tim2 = Turtle(shape="turtle")
# tim2.color(colors[2])
# tim2.penup()
# tim2.goto(x=-230, y=-50)
#
# tim3 = Turtle(shape="turtle")
# tim3.color(colors[3])
# tim3.penup()
# tim3.goto(x=-230, y=0)
#
# tim4 = Turtle(shape="turtle")
# tim4.color(colors[4])
# tim4.penup()
# tim4.goto(x=-230, y=50)
#
# tim5 = Turtle(shape="turtle")
# tim5.color(colors[5])
# tim5.penup()
# tim5.goto(x=-230, y=100)

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index]) # get the colors from the list and assign one by one
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index]) # move forward
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230: # come to the winning line
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet: # check the color of the winning turtle and user selected color
                print(f"You've won! the {winning_color} turtle is the winner")
            else:
                print(f"You've lose! the {winning_color} turtle is the winner")

        rand_distance = random.randint(0, 10) # assign a number between 1 to 10
        turtle.forward(rand_distance) # move forward


screen.exitonclick()
