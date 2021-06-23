from turtle_brain import Turtle, Screen

todd = Turtle()
screen = Screen()


def move_forwards():
    todd.forward(10)


def move_backwards():
    todd.backward(10)


def move_counter_clock():
    todd.left(10)

def move_clock():
    todd.right(10)


def reset_screen():
    # my solution
    screen.resetscreen()

#     instructor's solution
#     todd.clear()
#     todd.penup()
#     todd.home()
#     todd.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=move_counter_clock)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clock)
screen.onkey(key="c", fun=reset_screen)
screen.exitonclick()
