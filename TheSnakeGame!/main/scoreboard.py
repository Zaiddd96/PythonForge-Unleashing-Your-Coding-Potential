from turtle import Turtle

FONT = ("courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.highscore = 0
        self.score = 0
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"\nHighScore: {self.highscore}\n   Score: {self.score}", align="center", font=FONT)

    def add_score(self):
        self.score += 1
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over!", align="center", font=FONT)

    def high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update()



