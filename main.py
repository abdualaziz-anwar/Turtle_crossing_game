import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.createCar()
    cars.moveCars()
    # detect collistion with car
    for x in cars.cars:
        if x.distance(player) < 20:
            print("oops")
            game_is_on = False
    # Reach End
    if player.ycor() > 280:
        player.start_over()
        cars.speed()
