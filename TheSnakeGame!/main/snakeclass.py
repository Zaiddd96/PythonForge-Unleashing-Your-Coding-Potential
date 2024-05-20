from turtle import Turtle

POSITION_XY = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for positions in POSITION_XY:
            self.add_snake(positions)

    def add_snake(self, position):
        t = Turtle("square")
        t.color("chartreuse")
        t.penup()
        t.goto(position)
        self.turtles.append(t)

    def extend(self):
        self.add_snake(self.turtles[-1].position())

    def move(self):
        for num in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[num - 1].xcor()
            y = self.turtles[num - 1].ycor()
            self.turtles[num].goto(x=x, y=y)
        self.head.forward(MOVE_DISTANCE)

    def restart(self):
        for seg in self.turtles:
            seg.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

