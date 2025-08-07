# ---- MAP: grid and HUD drawing ----
import pygame

def calculate_map_dimensions(window_width, window_height):
    """
    Compute the grid and game rectangle dimensions.
    """
    rect_x = int(window_width * 0.04)
    rect_y = int(window_height * 0.15)
    rect_width = int(window_width * 0.92)
    rect_height = int(window_height * 0.83)
    tile_size = max(10, int(window_width * 0.04))
    num_cols = rect_width // tile_size
    num_rows = rect_height // tile_size
    return rect_x, rect_y, rect_width, rect_height, tile_size, num_cols, num_rows

def draw_top_rectangle(screen, window_width, window_height):
    """
    Draw the top rectangle (HUD area).
    """
    top_rect_height = int(window_height * 0.1)
    pygame.draw.rect(screen, (74, 117, 44), (0, 0, window_width, top_rect_height))

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

def create_map(screen, window_width, window_height):
    """
    Draw the full map (background, HUD, grid).
    """
    screen.fill((87, 138, 52))
    rect_x, rect_y, rect_width, rect_height, tile_size, num_cols, num_rows = calculate_map_dimensions(window_width, window_height)
    draw_top_rectangle(screen, window_width, window_height)
    draw_checkerboard(screen, rect_x, rect_y, rect_width, rect_height, tile_size, num_cols, num_rows)
    return rect_x, rect_y, rect_width, rect_height, tile_size, num_cols, num_rows