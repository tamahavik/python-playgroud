# import colorgram
#
# colors = colorgram.extract("images.jpg", 30)
# list_color = []
# for color in colors:
#     tup = (color.rgb.r, color.rgb.g, color.rgb.b)
#     list_color.append(tup)
#
# print(list_color)

from turtle import Turtle, Screen
import random

color_list = [(107, 110, 128), (139, 141, 154), (237, 214, 226), (224, 213, 114), (218, 235, 222), (180, 73, 32),
              (205, 146, 175), (182, 159, 35), (104, 110, 172), (194, 13, 3), (15, 17, 62), (14, 35, 16),
              (228, 167, 197), (220, 81, 55), (32, 32, 12), (198, 8, 19), (42, 44, 121), (155, 173, 159), (142, 74, 88),
              (234, 172, 159), (211, 72, 93), (88, 106, 91), (179, 181, 220), (223, 209, 16), (38, 17, 37),
              (72, 78, 33), (177, 204, 178)]
x = -200
y = -200
t = Turtle()
t.penup()
t.hideturtle()
t.setposition(x, y)
t.speed("fastest")
s = Screen()
s.colormode(255)


def shift_position():
    global x, y
    x = -200
    y += 50


def create_dot():
    color = random.choice(color_list)
    t.dot(20, color)
    t.forward(50)


for _ in range(10):
    for _ in range(10):
        create_dot()
    shift_position()
    t.setposition(x, y)

s.exitonclick()
