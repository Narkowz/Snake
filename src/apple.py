# ---- APPLE MANAGEMENT ----
import src.utils as utils
import pygame

def load_apple_image():
    return utils.load_image("assets/apple.png")

def draw_apple(screen, apple_image, rect_x, rect_y, tile_size, apple_col, apple_row):
    """
    Draw the apple on the grid at position (apple_col, apple_row).
    """
    if apple_image:
        original_width, original_height = apple_image.get_size()
        new_height = tile_size
        new_width = int((original_width / original_height) * new_height)
        scaled_apple = pygame.transform.smoothscale(apple_image, (new_width, new_height))
        apple_x = rect_x + apple_col * tile_size
        apple_y = rect_y + apple_row * tile_size
        apple_x += (tile_size - new_width) // 2
        apple_y += (tile_size - new_height) // 2
        screen.blit(scaled_apple, (apple_x, apple_y))
    else:
        window_width, window_height = pygame.display.get_window_size()
        pygame.draw.circle(screen, (255, 0, 0), (window_width // 2, window_height // 2), tile_size // 2) 