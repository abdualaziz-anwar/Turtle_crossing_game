from turtle import Turtle, speed
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def createCar(self):
        car_chance = random.randint(1,6)
        if car_chance == 1 :
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_position = random.randint(-250 , 250)
            new_car.goto(300 , y_position)
            self.cars.append(new_car)


    def moveCars(self):
        for x in self.cars:
            x.backward(self.car_speed)

    def speed(self):
        self.car_speed += MOVE_INCREMENT