from turtle_model import TurtleRacer, UserSettings
from turtle import Screen
import random

class TurtleCreator:
    def __init__(self):
        self.turtle_racer = TurtleRacer()

    def turtle_race(self):
        is_race_on = False
        user = UserSettings()
        screen = Screen()
        screen.setup(user.width, user.height)
        user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
        turtle_index = self.turtle_racer.all_turtles()
        if user_bet:
            is_race_on = True
        while is_race_on:
            for turtle in turtle_index:
                if turtle.xcor() >230:
                    is_race_on = False
                    winning_color = turtle.pencolor()
                    if winning_color == user_bet:
                        print(f"You've won! The {winning_color} turtle is the winner!")
                    else:
                        print(f"You've lost! Sooo stuuupid. {winning_color} turtle won.")
                rand_distance = random.randint(0, 10)
                turtle.forward(rand_distance)

        screen.exitonclick()

