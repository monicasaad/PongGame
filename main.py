# import required modules
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# create screen object from Screen class and set background color and screen size
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
# turn off animations at start to see paddles created at same time
screen.tracer(0)

# create right and left paddle objects
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
# create ball object from Ball class
ball = Ball()
# create scoreboard object from Scoreboard class
scoreboard = Scoreboard()

# make screen listen for events
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# update screen manually while game is running since tracer initially turned off
game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect when right paddle misses
    if ball.xcor() > 380:
        # add point to left side
        scoreboard.l_point()
        ball.reset_position()

    # detect when left paddle misses
    if ball.xcor() < -380:
        # add point to right side
        scoreboard.r_point()
        ball.reset_position()

# keep screen up until clicked
screen.exitonclick()
