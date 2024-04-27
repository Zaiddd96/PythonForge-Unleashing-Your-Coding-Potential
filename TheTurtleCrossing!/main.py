import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car = CarManager()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_cars()
    car.move()

    for unit in car.cars:
        if unit.distance(player) < 20:
            game_is_on = False

    if player.at_finish_line():
        player.new_level()
        car.increase_speed()


screen.exitonclick()
