from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.re_score()

    def re_score(self):
        self.clear()
        self.write(f"SCORE : {self.r_score} / {self.l_score}", move=False, align="center", font=("Arial", 14, "normal"))

    def lre_score(self):
        self.l_score += 1
        return self.l_score

    def rre_score(self):
        self.r_score += 1
        return self.r_score

    def game_over(self):
        if self.l_score == 5 or self.r_score == 5:
            self.goto(0, 0)
            self.color("RED")
            str = f"GAME OVER \n SCORE : {self.r_score} / {self.l_score}"
            self.write(str, move=False, align="center", font=("Arial", 28, "normal"))
