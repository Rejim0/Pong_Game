from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# create game screen
screen = Screen()
screen.tracer(0)  # turn off auto animation, we control it manually

# create paddles on right and left side
right_paddle = Paddle(350,0)
left_paddle = Paddle(-350,0)

# create ball and score objects
ball = Ball()
score = Score()

# listen for keyboard input
screen.listen()
screen.onkey(right_paddle.up,"Up")     # move right paddle up
screen.onkey(right_paddle.down,"Down") # move right paddle down
screen.onkey(left_paddle.up,"w")       # move left paddle up
screen.onkey(left_paddle.down,"s  ")   # move left paddle down

# screen setup
screen.bgcolor("black")
screen.setup(width = 800, height = 600)
screen.title("Pong Game")

# game loop starts
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)  # control game speed
    screen.update()              # update screen manually
    ball.move()                  # move the ball

    # check collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # check collision with paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50  and ball.xcor() < -320:
        ball.bounce_x()

    # if ball goes past right side → left player scores
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # if ball goes past left side → right player scores
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

# keep window open until click
screen.exitonclick()