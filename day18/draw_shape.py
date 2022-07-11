from turtle import Turtle, Screen
import random

color = ["blue", "red", "chartreuse", "yellow green", "yellow", "moccasin", "dark orange", "dark red", "rosy brown",
         "deep pink", "purple", "thistle"]

t = Turtle()
t.shape("turtle")
t.color("red")


def draw_shape(num_side):
    angel = 360 / num_side
    for _ in range(i):
        t.forward(100)
        t.right(angel)


for i in range(3, 11):
    t.color(random.choice(color))
    draw_shape(i)

screen = Screen()
screen.exitonclick()
