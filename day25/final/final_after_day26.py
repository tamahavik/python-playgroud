from turtle import Turtle, Screen, shape
import pandas

IMAGE_PATH = "blank_states_img.gif"

s = Screen()
s.title("U.S States Game")
s.addshape(IMAGE_PATH)
shape(IMAGE_PATH)

data = pandas.read_csv("./50_states.csv")
all_state = data.state.to_list()
guess_state = []

is_game_on = True
while is_game_on:
    answer_state = s.textinput(title=f"{len(guess_state)}/{len(all_state)} guest the state",
                               prompt="what another states name?").title()
    if answer_state == "Exit":
        missing_state = [state for state in all_state if state not in guess_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("./missing_state.csv")
        break

    if answer_state.title() in all_state:
        guess_state.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(state_data.state.item())

s.exitonclick()
