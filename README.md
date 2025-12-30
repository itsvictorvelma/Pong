# 🏓 Pong (Python / Turtle)

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OOP](https://img.shields.io/badge/OOP-Practice-informational)
![Status](https://img.shields.io/badge/Status-Complete-success)
---

## 🎮 Gameplay
Classic Pong built with Python Turtle.

## 🧠 Focus
OOP fundamentals, game loop control, collision logic.

## 🎛 Controls
- W / S — Left paddle  
- ↑ / ↓ — Right paddle

## Difficulty

Chosen at launch:

- `1` — Easy  
- `2` — Normal  
- `3` — Hard  

Defaults to Easy if input is invalid or skipped.

---

## Project Structure
``` 
├── main.py # Game setup and main loop
├── ball.py # Ball movement and collisions
├── paddles.py # Paddle behavior and bounds
├── scoreboard.py # Score tracking and win screen
├── input_state.py # Keyboard state handling
└── README.md

Each component owns its own state.  
No tightly coupled logic or shared mutable globals.
```

## 📽 Demo

#### for the sake of the demo - points_needed_to_win = 4
**Gameplay Video**

https://github.com/user-attachments/assets/b9efa27a-9f67-44b7-b653-b0491df8b1f2

**Screenshots**

<img width="806" height="643" alt="Screenshot from 2025-12-30 15-09-23" src="https://github.com/user-attachments/assets/c7e55783-abff-4cd9-b466-c04a1da49c95" />
<img width="806" height="643" alt="Screenshot from 2025-12-30 15-10-28" src="https://github.com/user-attachments/assets/ca184b10-11d9-4849-aa80-adc6b4253c69" />
