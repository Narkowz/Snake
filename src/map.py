# ---- MAP: grid and HUD drawing ----
import pygame
import src.config as config

def calculate_map_dimensions():
    """
    Compute the grid and game rectangle dimensions using config.
    """
    rect_x = int(config.WINDOW_WIDTH * 0.04)
    rect_y = int(config.WINDOW_HEIGHT * 0.15)
    rect_width = int(config.WINDOW_WIDTH * 0.92)
    rect_height = int(config.WINDOW_HEIGHT * 0.83)
    # Use config for grid size
    tile_size_x = rect_width // config.GRID_COLS
    tile_size_y = rect_height // config.GRID_ROWS
    tile_size = min(tile_size_x, tile_size_y)
    num_cols = config.GRID_COLS
    num_rows = config.GRID_ROWS
    return rect_x, rect_y, rect_width, rect_height, tile_size, num_cols, num_rows

def draw_top_rectangle(screen):
    """
    Draw the top rectangle (HUD area).
    """
    top_rect_height = int(config.WINDOW_HEIGHT * 0.1)
    pygame.draw.rect(screen, (74, 117, 44), (0, 0, config.WINDOW_WIDTH, top_rect_height))

def draw_checkerboard(screen, rect_x, rect_y, rect_width, rect_height, tile_size, num_cols, num_rows):
    """
    Draw the game grid as a checkerboard.
    """
    for row in range(num_rows):
        for col in range(num_cols):
            color = (170, 215, 81) if (row + col) % 2 == 0 else (162, 209, 73)
            x = rect_x + col * tile_size
            y = rect_y + row * tile_size
            pygame.draw.rect(screen, color, (x, y, tile_size, tile_size))

def create_map(screen):
    """
    Draw the full map (background, HUD, grid).
    """
    screen.fill((87, 138, 52))
    rect_x, rect_y, rect_width, rect_height, tile_size, num_cols, num_rows = calculate_map_dimensions()
    draw_top_rectangle(screen)
    draw_checkerboard(screen, rect_x, rect_y, rect_width, rect_height, tile_size, num_cols, num_rows)
    return rect_x, rect_y, rect_width, rect_height, tile_size, num_cols, num_rows