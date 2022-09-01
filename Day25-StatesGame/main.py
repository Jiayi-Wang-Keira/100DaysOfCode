import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states)<50:
    answer = screen.textinput(title=f"{len(guess_states)}/50 states correct", prompt="Please enter a state: ").title()
    if answer in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        new_x = int(data[data['state'] == answer].x)
        new_y = int(data[data['state'] == answer].y)
        t.goto(new_x, new_y)
        t.write(answer)
        guess_states.append(answer)

    if answer.lower() == "exit":
        with open("states_to_learn.csv", mode="w") as file:
            for state in all_states:
                if state not in guess_states:
                    file.write(state + "\n")
        break




screen.exitonclick()
