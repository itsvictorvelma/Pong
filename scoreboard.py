from turtle import Turtle

# Font + alignment used for all scoreboard text
FONT = ("Courier", 30, "normal")
ALIGNMENT = "center"


class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()

        # Internal score state (this is what actually increments)
        self.score = 0

        # Turtle setup for text-only rendering
        self.penup()
        self.goto(x, y)
        self.color("white")
        self.speed("fastest")
        self.hideturtle()

        # Initial score render
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increment score and refresh the on-screen value"""
        # Need to clear before rewriting or text will stack
        self.clear()
        self.score += 1
        self.write(self.score, align=ALIGNMENT, font=FONT)

    def game_over(self, player):
        """Displays final game over message in the center"""
        # Reposition to center for end screen
        self.goto(0, 0)
        self.write(f"Game Over. {player} Wins", align=ALIGNMENT, font=FONT)
