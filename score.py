from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")      # text color
        self.penup()
        self.hideturtle()        # hide turtle shape
        self.l_score = 0         # left player score
        self.r_score = 0         # right player score
        self.update_score()      # display score

    def update_score(self):
        self.clear()  # clear old score
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        # increase left player score
        self.l_score += 1
        self.update_score()

    def r_point(self):
        # increase right player score
        self.r_score += 1
        self.update_score()