from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,250)
        self.user_score = 0
        self.computer_score = 0
        self.display()

    def score_update(self):
        self.clear()
        self.display()

    def display(self):
        self.write(f"{self.user_score} : {self.computer_score}",align="center", font=("Calibri", 20, "normal"))