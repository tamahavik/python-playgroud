from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.bgcolor("black")
s.setup(width=800, height=600)
s.title("Pong")
s.tracer(0)

player_1 = Paddle((-350, 0))
player_2 = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

s.listen()
s.onkey(player_1.go_up, "w")
s.onkey(player_1.go_down, "s")
s.onkey(player_2.go_up, "Up")
s.onkey(player_2.go_down, "Down")

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    s.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player_2) < 50 and ball.xcor() > 320 or ball.distance(player_1) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.p1_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.p2_point()

s.exitonclick()
