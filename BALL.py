from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, 0)
        self.setheading(180)
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.y_move = 10
        self.x_move = 10

    def walk(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x=x_pos, y=y_pos)

    def bounce(self, z):
        if z == 'y':
            self.y_move *= -1
        elif z == 'x':
            self.x_move *= -1
