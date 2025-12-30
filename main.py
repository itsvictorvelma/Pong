from turtle import Screen
from paddles import Paddle, PADDLE_HALF_WIDTH, PADDLE_HALF_HEIGHT
from ball import RADIUS, Ball
from input_state import InputState
from scoreboard import Score

# ----------------------------
# Screen setup (static config)
# ----------------------------
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong innit")

# Turn off auto refresh so we control frames manually
screen.tracer(0)

# Disable window resizing (keeps collision math from drifting)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.resizable(False, False)

# ----------------------------
# Core game objects
# ----------------------------

# Paddles sit just inside the screen edges
l_paddle = Paddle(pos=(-390, 0))
r_paddle = Paddle(pos=(380, 0))

# Ball handles all movement + collision logic
ball = Ball()

# ----------------------------
# Difficulty select (runs once)
# ----------------------------
# textinput is blocking, so this MUST happen before the game loop
difficulty = screen.textinput(
    title="Difficulty", prompt="Easy (1) | Normal (2) | Hard (3)"
)
ball.choose_difficulty(difficulty)

# ----------------------------
# Scoreboards
# ----------------------------
# Created once and persist for the entire match
score_l = Score(-160, 240)
score_r = Score(160, 240)

# ----------------------------
# Input handling
# ----------------------------

# Tracks key states instead of reacting to single presses
input_state = InputState()

KEYS = {"w", "s", "Up", "Down"}

# Init all keys as not pressed + bind press/release handlers
for key in KEYS:
    input_state.keys[key] = False

    screen.onkeypress(
        lambda k=key: input_state.keys.__setitem__(k, True),
        key,
    )

    screen.onkeyrelease(
        lambda k=key: input_state.keys.__setitem__(k, False),
        key,
    )

# ----------------------------
# Game loop control
# ----------------------------
game_is_on = True


def game_loop():
    global game_is_on

    # Hard exit once win condition is hit
    if not game_is_on:
        return

    # ------------------------
    # Paddle movement
    # ------------------------
    if input_state.keys["Up"]:
        r_paddle.up()

    if input_state.keys["Down"]:
        r_paddle.down()

    if input_state.keys["w"]:
        l_paddle.up()

    if input_state.keys["s"]:
        l_paddle.down()

    # ------------------------
    # Ball movement + walls
    # ------------------------
    ball.move_ball()
    ball.check_wall_collision()

    # ------------------------
    # Paddle collisions
    # ------------------------
    # Right paddle collision check
    if (
        ball.xcor() + RADIUS >= r_paddle.xcor() - PADDLE_HALF_WIDTH
        and abs(ball.ycor() - r_paddle.ycor()) <= PADDLE_HALF_HEIGHT
    ):
        # Push ball out first to avoid sticking / double bounces
        ball.setx(r_paddle.xcor() - PADDLE_HALF_WIDTH - RADIUS)
        ball.bounce_x()

    # Left paddle collision check
    if (
        ball.xcor() - RADIUS <= l_paddle.xcor() + PADDLE_HALF_WIDTH
        and abs(ball.ycor() - l_paddle.ycor()) <= PADDLE_HALF_HEIGHT
    ):
        ball.setx(l_paddle.xcor() + PADDLE_HALF_WIDTH + RADIUS)
        ball.bounce_x()

    # ------------------------
    # Scoring + resets
    # ------------------------
    if ball.check_out_of_bounds_right():
        ball.reset()
        score_l.increase_score()

    if ball.check_out_of_bounds_left():
        ball.reset()
        score_r.increase_score()

    # ------------------------
    # Win condition
    # ------------------------
    if score_r.score == 11:
        game_is_on = False
        ball.hideturtle()
        score_r.game_over("Player 2")

    if score_l.score == 11:
        game_is_on = False
        ball.hideturtle()
        score_r.game_over("Player 1")

    # ------------------------
    # Frame update
    # ------------------------
    screen.update()
    screen.ontimer(game_loop, 16)  # ~60fps-ish


# ----------------------------
# Boot sequence
# ----------------------------
screen.listen()
game_loop()
screen.mainloop()
