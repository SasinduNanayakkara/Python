import turtle
import pandas
screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_name = data.state
state_list = state_name.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} / 50 Guessed the State",
                                    prompt="What's another state name",).title()

    if answer_state == "Exit":
        # missing_state = []
        #     for states in state_list:
        #         if states not in guessed_states:
        #             missing_state.append(states)
        #     print(missing_state)
        #     new_data = pandas.DataFrame(missing_state)
        #     new_data.to_csv("learn_to_state.csv")
        missing_state = [states for states in state_list if states not in guessed_states]
        print(missing_state)
        # new_data = pandas.DataFrame(missing_state)
        # new_data.to_csv("learn_to_state.csv")

        break


    if answer_state in state_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)  # state_data.state.item()


