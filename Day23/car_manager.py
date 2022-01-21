from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.enemies = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(x=300, y=random.randrange(-250, 250))
            new_car.speed(0.1)
            self.enemies.append(new_car)
        self.move()

    def move(self):
        for car in self.enemies:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += STARTING_MOVE_DISTANCE
        self.create_car()
