#!/bin/env python3

import sys
import pygame
import numpy

#- Settings
cell_around = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
color_live = (0, 0, 0)
color_dead = (255, 255, 255)

# ========================================================
# USEFUL FUNCTIONS
# ========================================================

#- Init window
def init_window(x, y, size):
    pygame.init()
    screen = pygame.display.set_mode((x, y))
    pygame.display.set_caption("Game of life")
    width, height = screen.get_size()
    cols = width // size
    rows = height // size
    return screen, cols, rows

#- Create cells tab
def create_cells(cols, rows):
    cells = numpy.zeros((cols, rows), dtype=int)
    return cells

#- Check is cell can live
def can_live(cell, i, j):
    around = sum(cell[i + x, j + y] for x, y in cell_around
                   if 0 <= i + x < cell.shape[0] and 0 <= j + y < cell.shape[1])

    if cell[i, j] == 1:
        return 1 if 2 <= around <= 3 else 0
    else:
        return 1 if around == 3 else 0

#- Update cells tab
def update_cells(grid):
    new_grid = grid.copy()

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            new_grid[i, j] = can_live(grid, i, j)
    return new_grid

#- Draw cells
def draw_cells(screen, cells, size, grid):
    #- Set background
    screen.fill(color_dead)

    #- Set cells
    for x in range(cells.shape[0]):
        for y in range(cells.shape[1]):
            color = color_live if cells[x, y] else color_dead
            pygame.draw.rect(screen, color, (x * size, y * size, size, size))

    #- Set grid
    if grid:
        for i in range(cells.shape[0] + 1):
            pygame.draw.line(screen, (128, 128, 128), (i * size, 0), (i * size, cells.shape[1] * size))
        for j in range(cells.shape[1] + 1):
            pygame.draw.line(screen, (128, 128, 128), (0, j * size), (cells.shape[0] * size, j * size))

    #- Display
    pygame.display.flip()

# ========================================================
# GAME OF LIFE FUNCTION
# ========================================================

def game_of_life(argv):
    running = True
    pause = True
    interval = 100
    interval_update = pygame.time.get_ticks()
    clock = pygame.time.Clock()

    #- Error handling
    if len(argv) != 5:
        print("Usage: ./game_of_life [win_x] [win_y] [cell_size] [grid ?]")
        exit(84)

    try:
        x = int(argv[1])
        y = int(argv[2])
        size = int(argv[3])
        grid = False if argv[4].lower() == "false" else True
    except ValueError:
        print("Usage: ./game_of_life [win_x] [win_y] [cell_size] [grid ?]")
        exit(84)

    #- Set window
    screen, cols, rows = init_window(x, y, size)

    #- Set cells
    cells = create_cells(cols, rows)

    #- Loop
    while running:
        #- Events : Launch and reload game of life
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pause = not pause
                elif event.key == pygame.K_r:
                    cells.fill(0)
                    pause = True

        #- Add cell if user click
        if pygame.mouse.get_pressed()[0] and pause:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            try:
                cells[mouse_x // size, mouse_y // size] = 1
            except:
                pass

        #- Update cells if program is paused
        if not pause:
            current_time = pygame.time.get_ticks()
            if current_time - interval_update > interval:
                cells = update_cells(cells)
                interval_update = current_time

        #- Draw cells
        draw_cells(screen, cells, size, grid)

        #- Set clock tick
        clock.tick(120)

    #- Quit window
    pygame.quit()

# ========================================================
# MAIN
# ========================================================

if __name__ == "__main__":
    game_of_life(sys.argv)
