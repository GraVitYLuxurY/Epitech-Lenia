import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import pygame
import numpy as np
from scipy.ndimage import convolve


# Grid configuration
CELL_SIZE = 2

# Lenia parameters
TIME_STEP = 0.1
MU = 0.5
SIGMA = 0.015

# Initialize Pygame
def init_window(size):
    pygame.init()
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption('Lenia')
    return screen

# Initialize Gaussian Kernel
def gaussian_kernel(size, sigma):
    kernel = np.fromfunction(
        lambda x, y: np.exp(
            -((x - size // 2) ** 2 + (y - size // 2) ** 2) / (2 * sigma ** 2)),
                (size, size))
    return kernel / np.sum(kernel)

# Update gride cells
def update(grid, kernel):
    conv = convolve(grid, kernel, mode='wrap')
    growth = np.exp(-((conv - MU) ** 2) / (2 * SIGMA ** 2))
    new_grid = np.clip(grid + TIME_STEP * (growth - 0.5), 0, 1)
    return new_grid

# Draw grid
def draw_grid(screen, grid, size):
    for x in range(size):
        for y in range(size):
            color = int(grid[x, y] * 255)
            pygame.draw.rect(
                screen,
                (color, color, color),
                pygame.Rect(y * CELL_SIZE, x * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main(av):
    try:
        size = int(av[1])
        cycles = int(av[2])
    except ValueError:
        print("Usage: ./lenia [size] [cycles]")
        exit(1)
    
    grid = np.random.rand(size, size)
    kernel = gaussian_kernel(7, 1.0)
    screen = init_window(size)
    clock = pygame.time.Clock()

    for cycle in range(cycles):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        grid = update(grid, kernel)
        draw_grid(screen, grid, size)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main(sys.argv)