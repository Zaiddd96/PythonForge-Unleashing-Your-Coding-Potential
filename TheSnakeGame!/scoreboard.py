from turtle import Turtle

# Constant for the font
FONT = ("courier", 15, "normal")

class Scoreboard(Turtle):
    """Class to represent the scoreboard in the game."""

    def __init__(self):
        """Initialize a new scoreboard object."""
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.hideturtle()
        self.update_score()

    def update_score(self):
        """Update the score on the scoreboard."""
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        """Increase the score by 1."""
        self.score += 1
        self.clear()
        self.update_score()

    def display_game_over(self):
        """Display 'Game Over' on the scoreboard."""
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=FONT)
