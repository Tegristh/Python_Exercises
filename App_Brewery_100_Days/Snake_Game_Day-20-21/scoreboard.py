from turtle import Turtle
FONT = "Futura"
FONT_SIZE = 12
FONT_TYPE = "bold"
ALIGNEMENT = "center"

with open("scores.txt") as scores:
    high_score = scores.read()


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.up()
        self.goto(x=0, y=280)
        self.score = 0
        self.high_score = int(high_score)
        self.update_scoreboard()

    def update_scoreboard(self,):
        self.clear()
        self.write(f"Score = {self.score}, high score = {self.high_score}", False, align=ALIGNEMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def score_up(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGNEMENT, font=(FONT, FONT_SIZE, FONT_TYPE))

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scores.txt", mode="w") as scores:
                scores.write(str(self.high_score))


