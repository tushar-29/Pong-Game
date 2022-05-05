from turtle import Screen, Turtle
from PONG_GAME.paddle import Paddle
from PONG_GAME.BALL import Ball
from PONG_GAME.Score_Board import ScoreBoard
from time import sleep


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title(titlestring="PONG GAME")
screen.tracer(0)
paddle_1 = Paddle(350)
paddle_2 = Paddle(-350)
ball = Ball()
score = ScoreBoard()


def draw_onscreen():
    pen = Turtle()
    pen.goto(0, 300)
    pen.right(90)
    pen.pensize(5)
    pen.hideturtle()
    pen.color("white")
    while pen.ycor() > -300:
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.forward(15)


screen.listen()
screen.onkeypress(fun=paddle_1.move_up, key="w")
screen.onkeypress(fun=paddle_1.move_down, key="s")
screen.onkeypress(fun=paddle_2.move_up, key="Up")
screen.onkeypress(fun=paddle_2.move_down, key="Down")

draw_onscreen()

while True:
    screen.update()
    sleep(0.05)
    ball.walk()
    score.re_score()
    score.game_over()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce('y')

    if ball.distance(paddle_1) < 25:
        ball.bounce('x')

    if ball.distance(paddle_2) < 25:
        ball.bounce('x')

    if ball.xcor() > 380:
        ball.bounce('x')
        ball.goto(0, 0)
        score.lre_score()

    if ball.xcor() < -380:
        ball.bounce('x')
        ball.goto(0, 0)
        score.rre_score()
