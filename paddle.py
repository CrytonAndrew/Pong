from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.setposition(position)
        self.shape("square")
        self.shapesize(stretch_wid=7, stretch_len=1)
        self.color("white")
        self.penup()

    def up(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 10
        self.goto(self.xcor(), new_y)
