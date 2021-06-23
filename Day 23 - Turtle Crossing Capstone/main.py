import time
from turtle import Screen

import player
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create turtle
# turtle should move only up when the "Up" key is pressed
turtle_player = Player()
carManager = CarManager()
scoreboard = Scoreboard()
count = 0

screen.listen()
screen.onkey(turtle_player.move_up, "Up")

game_is_on = True
while game_is_on:
    count += 1
    time.sleep(0.1)
    screen.update()

    # Enable cars to move
    # they should move from right to left on the screen
    carManager.move_car()

    # create cars
    # Cars should be randomly generated along the y-axis
    # create a car every 6 loops
    if count == 6:
        carManager.create_car()
        count = 0

    # detect when player turtle colliders with a car
    # whenever a car collides with the turtle, the game should stop at the "GAME OVER" screen
    for car in carManager.car_list:
        if turtle_player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # define what happens when the turtle hits the top of the screen
    # define the threshold for when the next level event triggers
    # the turtle should reset and the level should change increasing the speed of the cars
    # the level display in the corner of the screen should also update
    if turtle_player.ycor() > player.FINISH_LINE_Y:
        turtle_player.player_reset()
        carManager.increase_car_speed()
        scoreboard.add_score()

screen.exitonclick()
