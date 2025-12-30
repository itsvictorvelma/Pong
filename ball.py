from turtle import Turtle

# Ball + arena constants
RADIUS = 10
CIELING = 300
FLOOR = -300
R_WALL = 400
L_WALL = -400


class Ball(Turtle):
    def __init__(self):
        super().__init__()

        # Visual setup
        self.color("gold")
        self.shape("circle")
        self.penup()

        # Velocity components (direction + speed)
        self.dx = 7
        self.dy = 7

    def choose_difficulty(self, difficulty):
        """Set ball speed based on difficulty input"""
        difficulty_speeds = {
            "1": 5,
            "2": 7,
            "3": 10,
        }

        # Default to easy if input is invalid or cancelled
        speed = difficulty_speeds.get(difficulty or "1", 5)
        self.dx = int(speed)
        self.dy = int(speed)

    def move_ball(self):
        """Move ball based on current velocity"""
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self):
        """Invert vertical direction"""
        self.dy *= -1

    def bounce_x(self):
        """Invert horizontal direction"""
        self.dx *= -1

    def check_wall_collision(self):
        """Handle top/bottom wall collisions"""
        if self.ycor() >= CIELING - RADIUS:
            self.bounce_y()

        if self.ycor() <= FLOOR + RADIUS:
            self.bounce_y()

    def check_out_of_bounds_right(self):
        """Returns True if ball exits right side"""
        if self.xcor() >= R_WALL - RADIUS:
            return True

    def check_out_of_bounds_left(self):
        """Returns True if ball exits left side"""
        if self.xcor() <= L_WALL + RADIUS:
            return True

    def reset(self):
        """Reset ball to center and flip serve direction"""
        self.goto(0, 0)
        self.dx *= -1
