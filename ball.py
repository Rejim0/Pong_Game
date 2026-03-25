from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")     # ball shape
        self.color("white")      # ball color
        self.penup()             # no drawing line
        self.x_position = 10     # movement in x direction
        self.y_position = 10     # movement in y direction
        self.move_speed = 0.1    # speed of ball

    def move(self):
        # calculate new position based on current direction
        new_x = self.xcor()+ self.x_position
        new_y = self.ycor()+ self.y_position
        self.goto(new_x,new_y)   # move ball to new position

    def bounce_y(self):
        # reverse vertical direction when hitting top/bottom wall
        self.y_position *= -1

    def bounce_x(self):
        # reverse horizontal direction when hitting paddle
        self.x_position *= -1
        self.move_speed *= 0.9   # increase speed after bounce

    def reset_position(self):
        # bring ball back to center after score
        self.goto(0,0)
        self.move_speed = 0.1    # reset speed
        self.bounce_x()          # send ball to opposite direction