from turtle import Screen
from SnakeClass import Snake
from Food import Food
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(height=600, width=600)
s.bgcolor("black")
s.title("Snake Game!")
s.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.right, "Right")
s.onkey(snake.left, "Left")

game_on = True
while game_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 14:
        food.refresh()
        snake.extend()
        score.add_score()

    for part in snake.turtles[1:]:
        if snake.head.distance(part) < 10:
            score.high_score()
            snake.restart()

s.exitonclick()
