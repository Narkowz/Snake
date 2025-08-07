# ---- UTILS ----
import os
import random

def load_image(path):
    if os.path.exists(path):
        return __import__('pygame').image.load(path)
    else:
        print(f"Error: File {path} does not exist")
        return None

def get_random_free_position(num_cols, num_rows, forbidden_positions):
    """
    Returns a (col, row) position on the grid that is not in forbidden_positions.
    """
    positions = [(col, row) for col in range(num_cols) for row in range(num_rows) if (col, row) not in forbidden_positions]
    if positions:
        return random.choice(positions)
    else:
        return None 