import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.title("Racing game")
screen.tracer(0)
scoreboard.display_score()

player = Player()
carManager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.create_car()

    if player.ycor() > 280:
        scoreboard.update_score()
        player.start_position()
        carManager.level_up()

    for car in carManager.enemies:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()