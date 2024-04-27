from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_car = random.randint(1, 6)
        if random_car == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color("black", random.choice(COLORS))
            y = random.randint(-250, 250)
            new_car.goto(300, y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.backward(self.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

