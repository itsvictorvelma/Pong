from turtle import Turtle

TOP = 300
BOTTOM = -300
RADIUS = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("gold")
        self.shape("circle")
        self.penup()
        self.dx = 4
        self.dy = 4

    def move_ball(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1

    def check_wall_collision(self):
        if self.ycor() >= TOP - RADIUS:
            self.bounce_y()

        if self.ycor() <= BOTTOM + RADIUS:
            self.bounce_y()
