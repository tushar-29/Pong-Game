from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.left(90)
        self.shapesize(stretch_len=4, stretch_wid=1)
        self.location(x)

    def location(self, x):
        self.goto(x, 0)

    def move_up(self):
        if self.ycor() < 280:
            self.setheading(90)
            self.fd(30)
        else:
            self.backward(10)

    def move_down(self):
        if self.ycor() > -280:
            self.setheading(270)
            self.fd(30)
        else:
            self.backward(10)
