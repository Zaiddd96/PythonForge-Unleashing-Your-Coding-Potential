from turtle import Turtle

FONT = "Courier New"
TYPE = "bold"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.display_scores()

    def display_scores(self):
        self.clear()
        self.goto(-96, 180)
        self.write(self.left_score, align="center", font=(FONT, 35, TYPE))
        self.goto(96, 180)
        self.write(self.right_score, align="center", font=(FONT, 35, TYPE))

    def left_scores(self):
        self.left_score += 1
        self.display_scores()

    def right_scores(self):
        self.right_score += 1
        self.display_scores()

    def title(self):
        self.goto(0, 250)
        self.write(arg="Pixel Bounce🎮", align="center", font=(FONT, 30, TYPE))
