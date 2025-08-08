# Snake Game

A modern version of the classic Snake game built with Python and Pygame.  
The main objective: eat apples, grow longer, and avoid collisions!

## Project Structure

```
.
├── assets/
│   ├── apple.png
│   └── snake_trophy.png
├── src/
│   ├── apple.py        # Apple management and rendering
│   ├── config.py       # Game configuration (window/grid size, etc.)
│   ├── hud.py          # Score, HUD and trophy display
│   ├── map.py          # Grid and background drawing
│   ├── player.py       # Snake logic and movement
│   └── utils.py        # Utility functions (load images, random positions)
├── main.py             # Game loop and orchestration
├── README.md           # (You are here)
└── .gitignore
```

## How the Game Works

- **Initialization:**  
  The game sets up a scalable grid, a top HUD area, and loads the necessary images (snake, apple, trophies).

- **Gameplay:**  
  Control the snake using the arrow keys. Eat apples to grow longer and increase your score.  
  The top bar (HUD) shows your current score, number of trophies, and invulnerability status.

- **Map & Logic:**  
  The grid and HUD are dynamically sized to fit your window. Snake movement and collision detection are handled each tick.

- **Invulnerability / Cheat:**  
  Press `G` to toggle invulnerability mode (useful for testing).

- **Victory:**  
  Win by filling all available spaces. When you do, a victory message appears.

## Requirements

- Python 3.8+
- Pygame (`pip install pygame`)

## How to Run

```
python main.py
```

## Coming Soon

✨ **Automated bot: let an AI play Snake for you!**  
Stay tuned for upcoming bot development and AI features.

## License / Usage

You are free to use this project for personal or non-commercial projects.