import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


game_is_on = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("CadetBlue2")
screen.title("Turtle Crossing Game")
screen.tracer(0)
screen.listen()

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


def turn_off():
    global game_is_on
    game_is_on = False


screen.onkey(turtle.move, "Up")
screen.onkey(turn_off, "Escape")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    if turtle.ycor() > 280:
        scoreboard.lvl_up()
        car_manager.increase_speed()
        turtle.reinit()

    for car in car_manager.cars_list:
        if car.xcor() < 30 and car.distance(turtle) < 20:
            scoreboard.game_over()
            turn_off()

screen.exitonclick()
