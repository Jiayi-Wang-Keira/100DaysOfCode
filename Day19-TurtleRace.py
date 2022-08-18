from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
is_race_on = False

y_co = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_co)
    all_turtles.append(new_turtle)
    y_co += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win! The {winning_turtle} turtle wins the game!")
            else:
                print(f"You lose! The {winning_turtle} turtle wins the game!")
            break
        move_amount = randint(0, 10)
        turtle.forward(move_amount)


screen.exitonclick()