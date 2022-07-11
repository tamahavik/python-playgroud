from turtle import Turtle, Screen

t = Turtle()
s = Screen()


def move_forward():
    t.forward(10)


def move_backward():
    t.back(10)


def turn_right():
    new_heading = t.heading() + 10
    t.setheading(new_heading)


def turn_left():
    new_heading = t.heading() - 10
    t.setheading(new_heading)


def clear():
    t.clear()
    t.reset()


s.onkeypress(key="w", fun=move_forward)
s.onkeypress(key="s", fun=move_backward)
s.onkeypress(key="d", fun=turn_right)
s.onkeypress(key="a", fun=turn_left)
s.onkeypress(key="c", fun=clear)
s.listen()

s.exitonclick()
