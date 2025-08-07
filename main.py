import sys
# ---- IMPORTS & INIT ----
import pygame
import src.config as config
import src.map as map
import src.player as player
import src.apple as apple
import src.hud as hud
import src.utils as utils

# ---- INITIALIZATION ----
def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption("Snake game")
    apple_image = apple.load_apple_image()
    trophy_image = hud.load_trophy_image()
    rect_x, rect_y, rect_width, rect_height, tile_size, num_cols, num_rows = map.create_map(screen)
    snake = player.Snake(num_cols // 2, num_rows // 2, tile_size)
    apple_col, apple_row = utils.get_random_free_position(num_cols, num_rows, snake.get_body_positions())
    apples_eaten = 0
    trophy_count = 0
    invulnerable = False
    return {
        'screen': screen,
        'apple_image': apple_image,
        'trophy_image': trophy_image,
        'window_width': config.WINDOW_WIDTH,
        'window_height': config.WINDOW_HEIGHT,
        'rect_x': rect_x,
        'rect_y': rect_y,
        'tile_size': tile_size,
        'num_cols': num_cols,
        'num_rows': num_rows,
        'snake': snake,
        'apple_col': apple_col,
        'apple_row': apple_row,
        'apples_eaten': apples_eaten,
        'trophy_count': trophy_count,
        'invulnerable': invulnerable
    }

# ---- RENDERING ----
def render_all(state):
    top_rect_height = int(state['window_height'] * 0.1)
    map.create_map(state['screen'])
    hud.draw_hud(state['screen'], state['apple_image'], state['trophy_image'], state['apples_eaten'], state['trophy_count'], state['window_width'], top_rect_height, state['invulnerable'])
    apple.draw_apple(state['screen'], state['apple_image'], state['rect_x'], state['rect_y'], state['tile_size'], state['apple_col'], state['apple_row'])
    state['snake'].draw(state['screen'], state['rect_x'], state['rect_y'])
    pygame.display.flip()

# ---- GAME LOOP ----
def game_loop(state):
    clock = pygame.time.Clock()
    move_delay = 150
    last_move_time = pygame.time.get_ticks()
    running = True
    victory = False
    game_over = False
    while running:
        current_time = pygame.time.get_ticks()
        running, state['invulnerable'] = handle_events(state['snake'], state['invulnerable'])
        if current_time - last_move_time > move_delay:
            head_x, head_y = state['snake'].get_head_position()
            dir_x, dir_y = state['snake'].direction
            next_x = head_x + dir_x
            next_y = head_y + dir_y
            if state['invulnerable'] and not can_move(next_x, next_y, state['num_cols'], state['num_rows']):
                last_move_time = current_time
            else:
                apples_eaten, ate_apple, game_over = process_snake_move(
                    state['snake'], state['apple_col'], state['apple_row'], state['apples_eaten'], state['num_cols'], state['num_rows'], state['invulnerable'])
                state['apples_eaten'] = apples_eaten
                last_move_time = current_time
                if ate_apple:
                    pos = utils.get_random_free_position(state['num_cols'], state['num_rows'], state['snake'].get_body_positions())
                    if pos:
                        state['apple_col'], state['apple_row'] = pos
                    else:
                        victory = True
                        running = False
                if game_over:
                    print("Game Over!")
                    running = False
        render_all(state)
        clock.tick(60)
    if victory:
        show_victory(state['screen'], state['window_width'], state['window_height'])
        pygame.time.wait(2000)
        pygame.quit()
        return 0
    pygame.quit()
    return 1

# ---- VICTORY DISPLAY ----
def show_victory(screen, window_width, window_height):
    font = pygame.font.SysFont(None, 60)
    text = font.render("VICTORY!", True, (255, 215, 0))
    rect = text.get_rect(center=(window_width // 2, window_height // 2))
    screen.blit(text, rect)
    pygame.display.flip()

# ---- EVENTS & CHEAT MODE ----
def handle_events(snake, invulnerable):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            return False, invulnerable
        if event.type == pygame.KEYDOWN and event.key == pygame.K_g:
            invulnerable = not invulnerable
    keys = pygame.key.get_pressed()
    snake.handle_input(keys)
    return True, invulnerable

# ---- MOVEMENT & COLLISION LOGIC ----
def can_move(next_x, next_y, num_cols, num_rows):
    return 0 <= next_x < num_cols and 0 <= next_y < num_rows

def process_snake_move(snake, apple_col, apple_row, apples_eaten, num_cols, num_rows, invulnerable):
    head_x, head_y = snake.get_head_position()
    dir_x, dir_y = snake.direction
    next_x = head_x + dir_x
    next_y = head_y + dir_y
    ate_apple = False
    game_over = False
    if not invulnerable and not can_move(next_x, next_y, num_cols, num_rows):
        game_over = True
    elif invulnerable and not can_move(next_x, next_y, num_cols, num_rows):
        pass
    else:
        snake.move()
        if snake.get_head_position() == (apple_col, apple_row):
            apples_eaten += 1
            snake.grow()
            ate_apple = True
        if not invulnerable and snake.check_collision_with_self():
            game_over = True
    return apples_eaten, ate_apple, game_over

# ---- MAIN ----
def main():
    state = init_game()
    result = game_loop(state)
    sys.exit(result)

if __name__ == "__main__":
    main()
