# Turtle crossing road

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard_crossing import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
carmanager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move_cars()
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.update_score()
        carmanager.level_up()
    for car in carmanager.carlineup:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
