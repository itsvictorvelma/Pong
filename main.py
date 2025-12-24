from turtle import Screen
from paddles import Paddle, PADDLE_HALF_WIDTH, PADDLE_HALF_HEIGHT
from ball import RADIUS, Ball
from input_state import InputState

# Assigning values to screens attributes
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong innit")
screen.tracer(0)
screen.listen()

# Disabling window resize
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.resizable(False, False)

# assigning paddles
l_paddle = Paddle(pos=(-390, 0))
r_paddle = Paddle(pos=(380, 0))

# adding ball from Ball class
ball = Ball()

# Creating Controls

input_state = InputState()

KEYS = {"w", "s", "Up", "Down"}

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

# Game loop

game_is_on = True


def game_loop():
    global game_is_on

    if not game_is_on:
        return

    # movement logic

    if input_state.keys["Up"]:
        r_paddle.up()

    if input_state.keys["Down"]:
        r_paddle.down()

    if input_state.keys["w"]:
        l_paddle.up()

    if input_state.keys["s"]:
        l_paddle.down()

    ball.move_ball()  # init ball movement
    ball.check_wall_collision()

    # Right paddle collison logic

    if (
        ball.xcor() + RADIUS >= r_paddle.xcor() - PADDLE_HALF_WIDTH
        and abs(ball.ycor() - r_paddle.ycor()) <= PADDLE_HALF_HEIGHT
    ):
        ball.bounce_x()

    # Left paddle collision logic

    if (
        ball.xcor() - RADIUS <= l_paddle.xcor() + PADDLE_HALF_WIDTH
        and abs(ball.ycor() - l_paddle.ycor()) <= PADDLE_HALF_HEIGHT
    ):
        ball.bounce_x()

    screen.update()  # Refresh screen after each move
    screen.ontimer(game_loop, 16)  # Call loop again after 100ms


game_loop()
screen.mainloop()
