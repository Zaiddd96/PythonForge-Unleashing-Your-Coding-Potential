from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("goldenrod")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x, y)

    def up(self):
        y = self.ycor() + 20
        self.goto(self.xcor(), y)

    def down(self):
        y = self.ycor() - 20
        self.goto(self.xcor(), y)
