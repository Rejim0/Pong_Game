from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_cor,y_cor):
        super().__init__()
        self.paddle_attributes(x_cor,y_cor)  # set paddle design and position

    def up(self):
        # move paddle up
        self.goto(self.xcor(),self.ycor()+20)

    def down(self):
        # move paddle down
        self.goto(self.xcor(),self.ycor()-20)

    def paddle_attributes(self,x_cor,y_cor):
        # set paddle appearance
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(x_cor, y_cor)
        self.turtlesize(stretch_wid=5, stretch_len=1)  # make it long vertically