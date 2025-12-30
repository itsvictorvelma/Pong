class InputState:
    def __init__(self):
        # Tracks whether each control key is currently held down
        # This lets the game loop handle smooth movement instead of single key events
        self.keys = {
            "w": False,
            "s": False,
            "Up": False,
            "Down": False,
        }
