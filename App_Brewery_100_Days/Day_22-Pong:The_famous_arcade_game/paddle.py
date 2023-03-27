from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.setheading(90)
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(position)
        self.shapesize(stretch_len=5)

    def move_up(self):
        if self.ycor() < 255:
            self.forward(20)

    def move_down(self):
        if self.ycor() > -255:
            self.backward(20)
