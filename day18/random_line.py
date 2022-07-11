from turtle import Turtle, Screen
import random

color = ["blue", "red", "chartreuse", "yellow green", "yellow", "moccasin", "dark orange", "dark red", "rosy brown",
         "deep pink", "purple", "thistle"]

s = Screen()
s.colormode(255)

t = Turtle()
t.pensize(15)
t.speed("fastest")


def random_color():
    num = range(0, 256)
    r = random.choice(num)
    g = random.choice(num)
    b = random.choice(num)
    random_color_tup = (r, g, b)
    return random_color_tup


def random_move():
    change = random.choice(range(0, 4))
    angel = change * 90
    t.setheading(angel)
    t.pencolor(random_color())
    t.forward(30)


for _ in range(200):
    random_move()

s.exitonclick()
