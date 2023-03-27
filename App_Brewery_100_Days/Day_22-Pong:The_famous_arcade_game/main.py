from turtle import Screen
from screen import ScreenInit
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time


game_is_on = True


def turn_off():
    global game_is_on
    game_is_on = False


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong")
screen.tracer(0)

screen_init = ScreenInit()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "z")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(turn_off, "Escape")


while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce(direction="vertical")
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) \
            or (ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce(direction="horizontal")
        ball.give_move_speed()

    if ball.xcor() > 380:
        scoreboard.r_point()
        ball.reset_position()
    if ball.xcor() < -380:
        scoreboard.l_point()
        ball.reset_position()

    ball.move()

screen.exitonclick()
