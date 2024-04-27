from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.tracer(0)
s.setup(800, 600)
s.title("Pixel Bounce!")
s.bgcolor("RoyalBlue4")
right = Paddle(360, 0)
left = Paddle(-370, 0)
ball = Ball()
score = Scoreboard()


s.listen()
s.onkey(right.up, "Up")
s.onkey(right.down, "Down")
s.onkey(left.up, "w")
s.onkey(left.down, "s")
game = True
while game:
    s.update()
    ball.move()
    time.sleep(ball.inc_speed)
    score.title()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right) < 50 and ball.xcor() > 320 or ball.distance(left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset()
        score.left_scores()

    if ball.xcor() < -380:
        ball.reset()
        score.right_scores()

s.exitonclick()
