import sys
import pygame
import copy
import numpy as np

check_around = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
cell_size = 4
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def can_live(cell, i, j):
    cells_around = 0
    for pos in check_around:
        try:
            if i + pos[0] >= 0 and j + pos[1] >= 0:
                if cell[i + pos[0]][j + pos[1]] == 1:
                    cells_around += 1
        except IndexError:
            continue
    if cell[i][j] == 1:
        if cells_around < 2 or cells_around > 3:
            return 0
        else:
            return 1
    else:
        if cells_around == 3:
            return 1
        else:
            return 0

def draw_grid(grid, size, screen):
    for row in range(size):
        for col in range(size):
            color = WHITE if grid[row, col] else BLACK
            pygame.draw.rect(screen, color,
                pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size))

def game_of_life(grid):
    new_grid = copy.deepcopy(grid)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_grid[i][j] = can_live(grid, i, j)
    return new_grid

def main(av):
    if len(av) != 3:
        exit(84)

    try:
        size = int(av[1])
        cycles = int(av[2])
    except ValueError:
        exit(84)

    pygame.display.set_caption('Game of Life')
    screen = pygame.display.set_mode((size * cell_size, size * cell_size))
    grid = np.random.randint(2, size=(size, size))
    for i in range(cycles):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        grid = game_of_life(grid)
        draw_grid(grid, size, screen)
        pygame.display.flip()
        pygame.time.wait(500)

if __name__ == '__main__':
    main(sys.argv)