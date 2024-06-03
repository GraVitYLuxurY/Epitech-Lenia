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

# Initialize Gaussian Kernel
def gaussian_kernel(size, sigma):
    kernel = np.fromfunction(
        lambda x, y: np.exp(
            -((x - size // 2) ** 2 + (y - size // 2) ** 2) / (2 * sigma ** 2)),
                (size, size))
    return kernel / np.sum(kernel)

# Update gride cells
def update(grid, kernel, sigma, mu, time_step):
    conv = convolve(grid, kernel, mode='wrap')
    growth = np.exp(-((conv - mu) ** 2) / (2 * sigma ** 2))
    new_grid = np.clip(grid + time_step * (growth - 0.5), 0, 1)
    return new_grid

# Draw grid
def draw_grid(screen, grid, size, cell_size):
    for x in range(size):
        for y in range(size):
            color = int(grid[x, y] * 255)
            pygame.draw.rect(
                screen,
                (color, color, color),
                pygame.Rect(y * cell_size, x * cell_size, cell_size, cell_size))

def main(av):
    try:
        grid_size = int(av[1])
        cell_size = int(av[2])
        mu = float(av[3])
        sigma = float(av[4])
        time_step = float(av[5])
        cycles = int(av[6])
    except:
        print("Usage: ./lenia [grid size] [cell size] [mu] [sigma] [time step] [cycles]")
        exit(1)
    
    grid = np.random.rand(grid_size, grid_size)
    kernel = gaussian_kernel(7, 1.0)
    screen = init_window(grid_size)
    clock = pygame.time.Clock()

    for cycle in range(cycles):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        grid = update(grid, kernel, sigma, mu, time_step)
        draw_grid(screen, grid, grid_size, cell_size)
        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main(sys.argv)