from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.setposition(0, 0)
        self.penup()
        self.shape("circle")
        self.color("white")
        self.width = 20
        self.height = 20
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def movement(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_opposite(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_opposite()
        self.ball_speed = 0.1
