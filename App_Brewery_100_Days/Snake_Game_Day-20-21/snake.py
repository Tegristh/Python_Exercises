from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SHAPE = "square"
COLOR = "white"
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Segment(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.color(COLOR)
        self.penup()

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Segment()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def add_segment(self):
        new_segment = Segment()
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        new_segment.goto(new_x, new_y)
        self.segments.append(new_segment)

    def move(self):
        for squarenum in range((len(self.segments)-1), 0, -1):
            newX = self.segments[squarenum - 1].xcor()
            newY = self.segments[squarenum - 1].ycor()
            self.segments[squarenum].goto(newX, newY)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def go_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def go_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.segments:
            segment.goto(1600, 1600)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
