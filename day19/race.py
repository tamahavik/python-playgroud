from turtle import Turtle, Screen
import random

is_race_on = False
s = Screen()
s.setup(width=500, height=400)
user_bet = s.textinput(title="Make your bet", prompt="Which turtle will win the race? enter the color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtle = []

for i in range(len(colors)):
    posy = 75 - (i * 30)
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-240, y=posy)
    all_turtle.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        move = random.randint(0, 10)
        turtle.forward(move)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you won the winning color {winning_color} turtle is winner!")
            else:
                print(f"you lost the winning color {winning_color} turtle is winner!")
            is_race_on = False

s.exitonclick()
