from turtle import Turtle, Screen
from random import random, choice

tim = Turtle()

def random_color():
    r = random()
    b = random()
    g = random()
    rand_color = (r, g, b)
    return rand_color


tim.speed("fastest")
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot in range(1,101):
    tim.dot(20, random_color())
    tim.forward(50)

    if dot % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = Screen()
screen.exitonclick()
