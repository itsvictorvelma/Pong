from turtle import Turtle

# Vertical movement bounds for paddles
CIELING = 240
FLOOR = -240

# Used by collision logic elsewhere
PADDLE_HALF_HEIGHT = 50
PADDLE_HALF_WIDTH = 10


class Paddle(Turtle):
    def __init__(self, pos: tuple[int, int]):
        super().__init__()

        # Basic paddle appearance
        self.shape("square")
        self.color("white")

        # Stretch square into a vertical paddle
        self.shapesize(stretch_wid=5, stretch_len=1)

        self.penup()
        self.setpos(*pos)
        self.speed("fastest")

        # Movement values (dx unused for now, kept for symmetry)
        self.dx = 0
        self.dy = 16

    def up(self):
        """Move paddle up, clamped to cieling"""
        if self.ycor() < CIELING:
            self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def down(self):
        """Move paddle down, clamped to floor"""
        if self.ycor() > FLOOR:
            self.goto(self.xcor() - self.dx, self.ycor() - self.dy)
