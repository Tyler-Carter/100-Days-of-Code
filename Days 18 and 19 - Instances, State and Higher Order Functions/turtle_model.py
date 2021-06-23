from turtle_data import turtle_colors
from turtle import Turtle, Screen


# create turtle racer class
class TurtleRacer:
    # define class attributes
    def __init__(self):
        self.t_color = turtle_colors
        self.shape = "turtle"
        self.x_pos = -235
        self.y_pos = -100
        self.screen = Screen()
        self.width = 500
        self.height = 400

    def all_turtles(self):
        # create list of y coordinates instead of manually creating one
        y_pos = []
        while self.y_pos < 200:
            y_pos.append(self.y_pos)
            self.y_pos += 30
        # initiate the screen method from then Turtle module
        # set screen size based on user class
        self.screen.setup(self.width, self.height)
        # create turtles and create a list of their attributes
        turtle_index = []
        for turtles in range(len(turtle_colors)):
            new_turtle = Turtle(shape=self.shape)
            new_turtle.penup()
            new_turtle.color(self.t_color[turtles])
            new_turtle.goto(self.x_pos, y_pos[turtles])
            turtle_index.append(new_turtle)
        return turtle_index
