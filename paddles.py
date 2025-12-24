from turtle import Turtle

TOP = 240
BOTTOM = -240

PADDLE_HALF_HEIGHT = 50
PADDLE_HALF_WIDTH = 10


class Paddle(Turtle):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setpos(*pos)
        self.speed("fastest")
        self.dx = 0
        self.dy = 20

    def up(self):
        if self.ycor() < TOP:
            self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def down(self):
        if self.ycor() > BOTTOM:
            self.goto(self.xcor() - self.dx, self.ycor() - self.dy)
