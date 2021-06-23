import paddle
from turtle import Screen
from scoreboard import ScoreBoard
from ball import Ball
import time

## Module 1 - Create the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

'''
Module 2 Create and move a paddle and
Module 3 - create another paddle
'''
l_paddle, r_paddle = paddle.paddles()

## Module 4 - Create the ball and make it move
ball = Ball()
scoreboard = ScoreBoard()


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.ball_move()


    ## Module 5 - Detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        # needs to bounce
        ball.bounce_x()

    # Detect when R paddle misses
    if ball.xcor() > 380:
        # ball should continue in opposite direction
        ball.ball_reset()
        scoreboard.l_point()

    # Detect when L paddle misses
    if ball.xcor() < -380:
        # ball should continue in opposite direction
        ball.ball_reset()
        scoreboard.r_point()






## Module 6 - Detect collision with paddle

## Module 7 - Detect when paddle misses

## Module 8 - Keep Score

screen.exitonclick()
