# import required modules
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(xpos, ypos)
        self.showturtle()

    # method to move up paddle
    def go_up(self):
        # keep same x-pos, increase y-pos by 20
        self.goto(self.xcor(), self.ycor() + 30)

    # method to move down paddle
    def go_down(self):
        # keep same x-pos, decrease y-pos by 20
        self.goto(self.xcor(), self.ycor() - 30)
