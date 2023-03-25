from turtle import Turtle
import random
COLORS = ["blue", "red", "yellow", "green"]
SHAPES = ["turtle", "circle", "square", "arrow"]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.shape(random.choice(SHAPES))
        self.color(random.choice(COLORS))
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

