from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("data.txt") as data:
            self.highest_score = int(data.read())
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score} Highest Score: {self.highest_score}", align="center", font=("Calibri", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def reset(self):
        if self.score > self.highest_score:
            with open("data.txt", mode="w") as data:
                data.write(str(self.score))
            self.highest_score = self.score
        self.score = 0
        self.clear()
        self.update_score_board()
