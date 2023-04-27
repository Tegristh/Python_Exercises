import turtle
import pandas as pd

FONT = ("Arial", 10, 'normal')
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=800, height=600)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

found_list = []
t = turtle.Turtle()
t.hideturtle()
t.penup()

game_is_on = True

while game_is_on:
    score = len(found_list)
    answer_state = screen.textinput(title=f"{score}/50 states correct",
                                    prompt="What's another state's name?").title()
    if (answer_state in data["state"].to_list()) and (answer_state not in found_list):
        state = data[data["state"] == answer_state]
        new_x = state["x"].to_list()[0]
        new_y = state["y"].to_list()[0]
        t.goto(new_x, new_y)
        found_list.append(answer_state)
        t.write(answer_state, align="center", font=FONT)

    if answer_state == "Exit":
        to_learn = [state for state in data.state.tolist() if state not in found_list]
        export = pd.DataFrame(to_learn)
        export.to_csv("states_to_learn.csv")
        break


screen.exitonclick()
