from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("blue4")
        self.penup()
        self.hideturtle()
        self.print_level()

    def print_level(self):
        self.goto(-200, 250)
        self.write(f"level: {self.level}", align="center", font=FONT)

    def lvl_up(self):
        self.level += 1
        self.clear()
        self.print_level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
