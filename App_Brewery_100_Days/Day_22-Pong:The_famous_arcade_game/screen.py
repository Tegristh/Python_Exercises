from turtle import Turtle


class ScreenInit(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, -300)
        self.color("White")
        self.setheading(90)
        self.hideturtle()
        self.draw_middle_lane()
        self.speed("fastest")

    def draw_middle_lane(self):
        while self.ycor() < 300:
            self.pendown()
            self.forward(30)
            self.penup()
            self.forward(30)
