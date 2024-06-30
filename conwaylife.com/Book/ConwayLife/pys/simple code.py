import pygame
import numpy as np

# initial parameters
CELL_SIZE = 10
WIDTH, HEIGHT = 800, 600
BLACK, WHITH = (0, 0, 0), (255, 255, 255)

# initial pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Life")

# initial Grid
cols, rows = WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE
grid = np.random.choice([0, 1], size=(rows, cols))


def update_grid(grid):
    new_grid = grid.copy()
    for i in range(rows):
        for j in range(cols):
            state = grid[i, j]
            neighbors = sum(
                [
                    grid[i, (j - 1) % cols],
                    grid[i, (j + 1) % cols],
                    grid[(i - 1) % rows, j],
                    grid[(i + 1) % rows, j],
                    grid[(i - 1) % rows, (j - 1) % cols],
                    grid[(i - 1) % rows, (j + 1) % cols],
                    grid[(i + 1) % rows, (j - 1) % cols],
                    grid[(i + 1) % rows, (j + 1) % cols],
                ]
            )
            if state == 0 and neighbors == 3:
                new_grid[i, j] = 1
            elif state == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
    return new_grid


def draw_grid(grid):
    for i in range(rows):
        for j in range(cols):
            color = WHITH if grid[i, j] == 1 else BLACK
            pygame.draw.rect(
                screen, color, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE,
                                CELL_SIZE)
            )


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_grid(grid)
    grid = update_grid(grid)
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()
