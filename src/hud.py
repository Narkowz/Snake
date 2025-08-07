# ---- HUD MANAGEMENT ----
import pygame
import src.utils as utils

def load_trophy_image():
    return utils.load_image("assets/snake_trophy.png")

def draw_hud(screen, apple_image, trophy_image, apples_eaten, trophy_count, window_width, top_rect_height, invulnerable):
    """
    Draws the apple, score, trophy, and invulnerability status in the HUD.
    """
    font = pygame.font.SysFont(None, int(top_rect_height * 0.5))
    icon_size = int(top_rect_height * 0.7)
    margin = int(top_rect_height * 0.15)
    x = margin
    y = (top_rect_height - icon_size) // 2
    # Apple
    if apple_image:
        apple_icon = pygame.transform.smoothscale(apple_image, (icon_size, icon_size))
        screen.blit(apple_icon, (x, y))
    x += icon_size + margin
    # Score
    text = font.render(str(apples_eaten), True, (255, 255, 255))
    screen.blit(text, (x, y + icon_size // 6))
    x += text.get_width() + margin * 2
    # Trophy
    if trophy_image:
        trophy_icon = pygame.transform.smoothscale(trophy_image, (icon_size, icon_size))
        screen.blit(trophy_icon, (x, y))
    x += icon_size + margin
    trophy_text = font.render(str(trophy_count), True, (255, 255, 255))
    screen.blit(trophy_text, (x, y + icon_size // 6))
    # ---- Invulnerability display in the top right corner ----
    if invulnerable:
        small_font = pygame.font.SysFont(None, int(top_rect_height * 0.3))
        invuln_text = small_font.render("Invulnerability", True, (255, 255, 0))
        invuln_rect = invuln_text.get_rect(topright=(window_width - margin, margin))
        screen.blit(invuln_text, invuln_rect) 