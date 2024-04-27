from turtle import Turtle
import random

class Food(Turtle):
    """Class to represent the food in the game."""

    def __init__(self):
        """Initialize a new food object."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Move the food to a new random location."""
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(x=rand_x, y=rand_y)
