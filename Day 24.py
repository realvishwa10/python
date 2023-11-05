# Snake game advanced

from turtle import Screen
from snake_advanced import Snake
from food import Food
from scoreboard_advanced import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("The snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # checking distance between food and snake
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.add_score()
        snake.extend()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_scoreboard()
        snake.reset_snake()
        # scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # scoreboard.game_over()
            scoreboard.reset_scoreboard()
            snake.reset_snake()

screen.exitonclick()