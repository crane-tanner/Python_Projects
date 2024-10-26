from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")

screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
my_ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(my_ball.move_speed)
    my_ball.move()
    screen.update()

    # Detect collision
    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_y()

    # detect collision with paddle
    if (my_ball.distance(r_paddle) < 50 and my_ball.xcor() > 320
            or my_ball.distance(l_paddle) < 50 and my_ball.xcor() < -320):

        my_ball.bounce_x()

    # detect when r_paddle misses
    if my_ball.xcor() > 380:
        my_ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    # detect when l_paddle misses
    if my_ball.xcor() < -380:
        my_ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()



screen.exitonclick()
