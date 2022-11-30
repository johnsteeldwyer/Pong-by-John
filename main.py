# TODO: implement ball follow effect
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time as t

STARTING_POS = [(460, 0), (-460, 0)]

screen = Screen()
screen.setup(width=1000, height=650)
screen.bgpic("pong background.gif")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(STARTING_POS[0])
paddle_2 = Paddle(STARTING_POS[1])
# paddle_2.shapesize(14,.8,0)
ball = Ball()
scoreboard_l = Score("l")
scoreboard_r = Score("r")

screen.listen()
screen.onkey(paddle_1.up, "Up")
screen.onkey(paddle_1.down, "Down")
screen.onkey(paddle_2.up, "w")
screen.onkey(paddle_2.down, "s")

while True:
    # Refreshes the screen every ten miliseconds
    t.sleep(0.01)

    # If ball goes out of bounds, gives point to appropiate team
    if ball.xcor() > 490:
        scoreboard_l.score()
        ball.reset()
    if ball.xcor() < -490:
        scoreboard_r.score()
        ball.reset()

    # Ball bounce (for ceiling or floor)
    if ball.ycor() > 298 or ball.ycor() < -298:
        ball.bounce()

    # Calculates when volley occurs
    if (
        ball.distance(paddle_1) < 40
        and ball.xcor() > 452
        or ball.distance(paddle_2) < 40
        and ball.xcor() < -452
    ):
        ball.volley()
    ball.move()
    screen.update()

screen.exitonclick()
