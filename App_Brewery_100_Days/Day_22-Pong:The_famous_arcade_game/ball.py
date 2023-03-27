from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.setheading(45)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, direction):
        if direction == "vertical":
            self.y_move *= -1
        if direction == "horizontal":
            self.x_move *= -1

    def reset_position(self):
        self.x_move *= -1
        self.goto(0, 0)
        self.move_speed = 0.1

    def give_move_speed(self):
        self.move_speed *= 0.9
