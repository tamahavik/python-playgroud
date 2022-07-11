from turtle import Turtle, Screen
import random

t = Turtle()
t.speed("fastest")
s = Screen()
s.colormode(255)


def random_color():
    num = range(0, 256)
    r = random.choice(num)
    g = random.choice(num)
    b = random.choice(num)
    rand_color = (r, g, b)
    return rand_color


def create_circle(angel):
    t.setheading(angel)
    t.pencolor(random_color())
    t.circle(100)


for i in range(0, 360, 3):
    create_circle(i)

s.exitonclick()
