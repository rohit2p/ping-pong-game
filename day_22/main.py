from turtle import Screen
from padle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
# creating the screen
screen = Screen()
screen.setup(width= 800 , height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

# paddle obj
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
# key desigh
screen.listen()
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")

# score
score = Scoreboard()

# Run the game loop
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speeds)
    screen.update()
    ball.move()
    # detect collision with wall(upper) 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # detect collision with the paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if r misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    # detect if l misses the ball
    if ball.xcor() < - 380:
        ball.reset_position()
        score.r_point()

















screen.exitonclick()