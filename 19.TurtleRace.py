# turtle race
import random
from turtle import Turtle, Screen

"""Etch a sketch project"""
# timmy = Turtle()
# screen = Screen()
#
#
# def move_forward():
#     return timmy.forward(10)
#
#
# def move_backward():
#     return timmy.backward(10)
#
#
# def tilt_clockwise():
#     return timmy.right(30)
#
#
# def tilt_anticlockwise():
#     return timmy.left(30)
#
#
# def clear_timmy_drawing():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
#
#
# screen.listen(screen.onkey(key="w", fun=move_forward))
# screen.listen(screen.onkey(key="s", fun=move_backward))
# screen.listen(screen.onkey(key="d", fun=tilt_clockwise))
# screen.listen(screen.onkey(key="a", fun=tilt_anticlockwise))
# screen.listen(screen.onkey(key="c", fun=clear_timmy_drawing))
# screen.exitonclick()

"""Turtle Race"""
is_game_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Make your bet", prompt="Do you want to bet on the race? Enter a color("
                                                            "red/orange/yellow/green/blue/purple) : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = -120
all_turtles = []

for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(i)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    y_position += 40
    all_turtles.append(new_turtle)

if user_input:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_input.lower():
                print(f"You have Won! The {winning_turtle} turtle is the winner")
            else:
                print(f"You have Lost! The {winning_turtle} turtle is the winner")
        else:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)


screen.exitonclick()
