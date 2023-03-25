from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

game_is_on = True


def turnoff():
    global game_is_on
    scoreboard.update_high_score()
    scoreboard.game_over()
    game_is_on = False


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")
screen.onkey(turnoff, "Escape")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    if snake.head.distance(food) < 15:
        scoreboard.score_up()
        snake.add_segment()
        food.refresh()
    if snake.head.xcor() > 290:
        y = snake.head.ycor()
        snake.head.goto(x=-290, y=y)
    if snake.head.xcor() < -290:
        y = snake.head.ycor()
        snake.head.goto(x=290, y=y)
    if snake.head.ycor() > 290:
        x = snake.head.xcor()
        snake.head.goto(x=x, y=-290)
    if snake.head.ycor() < -290:
        x = snake.head.xcor()
        snake.head.goto(x=x, y=290)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
    snake.move()

screen.exitonclick()
