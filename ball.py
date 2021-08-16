from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + 10
        new_y = self.ycor() + 10
        self.goto(new_x, new_y)

    def move_sw(self):
        newx = self.xcor() + 10
        newy = self.ycor() - 10
        self.goto(newx, newy)
        self.write(self.xcor, align="left")