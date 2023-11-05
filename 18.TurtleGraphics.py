# Create Art
import turtle
from turtle import Turtle, Screen
import random
import colorgram

timmy = Turtle()
# timmy.shape("turtle")
timmy.color("steelblue")

"""Creating different shapes"""
# sides = 3
# while sides < 11:
#     angle = 360/sides
#     for i in range(sides):
#         timmy.right(angle)
#         timmy.forward(100)
#     sides += 1

"""Random walk"""
# walk = timmy
# walk.hideturtle()
# walk.pensize(15)
# walk.speed(0)
# initial = 0
# def random_color():
#     turtle.colormode(255)
#     R = random.randint(0, 255)
#     G = random.randint(0, 255)
#     B = random.randint(0, 255)
#     walk.color(R, G, B)
# def turn():
#     return random.choice([0, 90, 180, 270])
# while initial< 40:
#     random_color()
#     walk.forward(40)
#     walk.setheading(turn())
#     initial += 1

"""Spirograph"""
# def random_color():
#     turtle.colormode(255)
#     R = random.randint(0, 255)
#     G = random.randint(0, 255)
#     B = random.randint(0, 255)
#     timmy.color(R, G, B)
#
#
# position = 0
# while position <= 360:
#     timmy.setheading(position)
#     timmy.pensize()
#     random_color()
#     timmy.circle(100, 360)
#     position += 5

"""Extract colors from Hirst painting"""
# rgb_colors = []
# colors = colorgram.extract("image.jpg", 10)
# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
#
# print(rgb_colors)
turtle.colormode(255)
color_list = [(228, 243, 251), (226, 147, 98), (27, 103, 178), (161, 57, 90), (148, 79, 51), (226, 61, 96), (172, 21, 41)]
"""This part of code is used to move timmy to bottom of screen to start painting"""
timmy.penup()
timmy.setheading(210)
timmy.forward(350)
timmy.setheading(0)
timmy.pendown()
num_of_dots = 100

for dot_count in range(1, num_of_dots+1):
    random_color = random.choice(color_list)
    timmy.dot(20, random_color)
    timmy.penup()
    timmy.forward(50)
    timmy.pendown()

    if dot_count % 10 == 0:
        timmy.penup()
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)
        timmy.pendown()

timmy.speed("fastest")
screen = Screen()
screen.exitonclick()
