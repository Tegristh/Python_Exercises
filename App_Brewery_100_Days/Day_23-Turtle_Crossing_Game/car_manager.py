from turtle import Turtle
import random as r
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars_list = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()

    def create_car(self):
        random_chance = (r.randint(1, 10))
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(r.choice(COLORS))
            new_car.setheading(180)
            new_car.shapesize(stretch_len=2)
            y_position = r.randint(-250, 250)
            new_car.goto(x=300, y=y_position)
            new_car.move_speed = self.move_speed
            self.cars_list.append(new_car)

    def move(self):
        for cars in self.cars_list:
            new_x = cars.xcor() - self.move_speed
            new_y = cars.ycor()
            cars.goto(new_x, new_y)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
