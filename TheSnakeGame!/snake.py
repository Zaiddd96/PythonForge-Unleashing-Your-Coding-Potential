from turtle import Turtle

# Constants for initial positions and directions
INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP, DOWN, RIGHT, LEFT = 90, 270, 0, 180
MOVE_DISTANCE = 20

class Snake:
    """Class to represent a snake in the game."""

    def __init__(self):
        """Initialize a new snake object."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create a new snake."""
        for position in INITIAL_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake."""
        new_segment = Turtle("square")
        new_segment.color("chartreuse")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extend the snake by adding a new segment."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Move the snake forward."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Move the snake upwards."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Move the snake downwards."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Move the snake to the right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Move the snake to the left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
