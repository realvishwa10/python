# Ping pong game

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard_pong import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_paddle()
        ball.move_speed *= 0.9

    if ball.xcor() > 390:
        ball.reset_ball()
        ball.move_speed = 0.1
        scoreboard.left_score()

    if ball.xcor() < -390:
        ball.reset_ball()
        ball.move_speed = 0.1
        scoreboard.rght_score()

screen.exitonclick()