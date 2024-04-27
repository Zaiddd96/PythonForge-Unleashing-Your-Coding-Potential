from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("snow2")
        self.penup()
        self.x = 10
        self.y = 10
        self.inc_speed = 0.1

    def move(self):
        x = self.xcor() + self.x
        y = self.ycor() + self.y
        self.goto(x, y)

    def bounce_x(self):
        self.x *= -1
        self.inc_speed *= 0.9

    def bounce_y(self):
        self.y *= -1
        self.inc_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.inc_speed = 0.1
        self.bounce_x()
