from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

computer_paddle = Paddle((350,0))
user_paddle = Paddle((-350,0))
small_ball = Ball()
score_board = Score()

screen.listen()
screen.onkey(key="Up", fun=computer_paddle.up)
screen.onkey(key="Down", fun=computer_paddle.down)
screen.onkey(key="w", fun=user_paddle.up)
screen.onkey(key="s", fun=user_paddle.down)

game_is_on = True
while game_is_on:
    time.sleep(small_ball.ball_speed)
    small_ball.move()

    #detect collision with wall
    if small_ball.ycor() > 280 or small_ball.ycor() < -280:
        small_ball.bounce_y()

    #detect collision with computer paddle
    if small_ball.distance(computer_paddle) < 50 and small_ball.xcor()>340:
        small_ball.bounce_x()

    #detect collision with computer paddle
    if small_ball.distance(computer_paddle) < 50 and small_ball.xcor()>320 or small_ball.distance(user_paddle) < 50 and small_ball.xcor()<-320:
        small_ball.bounce_x()

    #detect ball out of bounds
    if small_ball.xcor()>380:
        small_ball.refresh()
        score_board.user_score += 1
        score_board.score_update()


    if small_ball.xcor()<-380:
        small_ball.refresh()
        score_board.computer_score += 1
        score_board.score_update()
    screen.update()

    if score_board.computer_score == 2 or score_board.user_score == 2:
        game_is_on = False

screen.exitonclick()