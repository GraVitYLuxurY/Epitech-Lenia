#!/bin/env python3

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import pygame
import numpy as np
from scipy.ndimage import convolve

# Initialize Pygame
def init_window(size):
    pygame.init()
    screen = pygame.display.set_mode((size, size))
    pygame.display.set_caption('Lenia')
    return screen

# Update grid cells
def update(grid, kernel, sigma, mu, time_step):
    conv = convolve(grid, kernel, mode='wrap')
    growth = np.exp(-((conv - mu) ** 2) / (2 * sigma ** 2))
    new_grid = np.clip(grid + time_step * (growth - grid), 0, 1)
    return new_grid

# Draw grid
def draw_grid(screen, grid):
    surface = pygame.surfarray.make_surface((grid * 255).astype(np.uint8))
    screen.blit(surface, (0, 0))
    pygame.display.flip()

def main(av):
    try:
        grid_size = int(av[1])
        mu = float(av[2])
        sigma = float(av[3])
        time_step = float(av[4])
    except:
        print("Usage: ./lenia [grid size] [mu] [sigma] [time step]")
        exit(1)
    
    grid = np.random.rand(grid_size, grid_size)
    kernel = np.ones((3, 3)) / 9
    screen = init_window(grid_size)
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        grid = update(grid, kernel, sigma, mu, time_step)
        draw_grid(screen, grid)
        clock.tick(60)

if __name__ == "__main__":
    main(sys.argv)