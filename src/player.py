# ---- SNAKE PLAYER ----
import pygame

class Snake:
    def __init__(self, start_x, start_y, tile_size):
        """
        Initialize the snake at the center of the grid.
        """
        self.tile_size = tile_size
        self.body = [(start_x, start_y)]
        self.direction = [1, 0]  # Right
        self.growing = False

    def handle_input(self, keys):
        """
        Handle keyboard input to change the snake's direction.
        """
        if keys[pygame.K_LEFT] and self.direction != [1, 0]:
            self.direction = [-1, 0]
        elif keys[pygame.K_RIGHT] and self.direction != [-1, 0]:
            self.direction = [1, 0]
        elif keys[pygame.K_UP] and self.direction != [0, 1]:
            self.direction = [0, -1]
        elif keys[pygame.K_DOWN] and self.direction != [0, -1]:
            self.direction = [0, 1]

    def move(self):
        """
        Move the snake in the current direction.
        """
        head_x, head_y = self.body[0]
        new_head_x = head_x + self.direction[0]
        new_head_y = head_y + self.direction[1]
        self.body.insert(0, (new_head_x, new_head_y))
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False

    def grow(self):
        """
        Make the snake grow by one segment.
        """
        self.growing = True

    def get_head_position(self):
        """
        Return the position of the snake's head.
        """
        return self.body[0]

    def get_body_positions(self):
        """
        Return all positions of the snake's body.
        """
        return self.body

    def check_collision_with_self(self):
        """
        Check if the snake collides with itself.
        """
        head = self.body[0]
        return head in self.body[1:]

    def draw(self, screen, rect_x, rect_y):
        """
        Draw the snake on the grid.
        """
        for i, (x, y) in enumerate(self.body):
            color = (78, 124, 246) if i == 0 else (64, 110, 224)
            screen_x = rect_x + x * self.tile_size
            screen_y = rect_y + y * self.tile_size
            pygame.draw.rect(screen, color, (screen_x, screen_y, self.tile_size, self.tile_size))
            pygame.draw.rect(screen, (78, 124, 246), (screen_x, screen_y, self.tile_size, self.tile_size), 1)