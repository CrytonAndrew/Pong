from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

paddle1 = Paddle((-350, 0))
paddle2 = Paddle((350, 0))
screen.listen()
screen.onkey(key="Up", fun=paddle1.up)
screen.onkey(key="Down", fun=paddle1.down)
screen.onkey(key="w", fun=paddle2.up)
screen.onkey(key="s", fun=paddle2.down)
ball = Ball()
score = Score()

game_is_on = True
time_speed = 0.1
while game_is_on:
    time.sleep(ball.ball_speed)  # Slows down the ball for every update on the screen
    screen.update()
    ball.movement()

    # Detect the collision with side walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect Ball Collision with paddle
    if ball.distance(paddle2) < 70 and ball.xcor() > 330:
        print("Collision to paddle")
        ball.bounce_opposite()
        score.increase_right()
        time_speed -= 0.1

    if ball.distance(paddle1) < 70 and ball.xcor() < -330:
        print("Collision to paddle")
        ball.bounce_opposite()
        score.increase_left()
        time_speed += 0.1

    # Detect right side miss:
    if ball.xcor() > 360:
        ball.reset_position()
        score.increase_left()

    # Detect left side miss:
    if ball.xcor() < -360:
        ball.reset_position()
        score.increase_right()


screen.exitonclick()
