import sys
import os
import time

cell_char = '#'
check_around = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]

def init_grid(file):
    with open(file) as f:
        return [[i for i in line.strip()] for line in f]

def empty_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == cell_char:
                return False
    return True

def can_live(cell, i, j):
    cells_around = 0
    for pos in check_around:
        try:
            if cell[i + pos[0]][j + pos[1]] == cell_char:
                cells_around += 1
        except:
            continue
    if (cell[i][j] == cell_char):
        if cells_around < 2 or cells_around > 3:
            return '.'
        else:
            return cell_char
    else:
        if cells_around == 3:
            return cell_char
        else:
            return '.'


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()

def game_of_life(grid):
    new_grid = grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_grid[i][j] = can_live(grid, i, j)
    return new_grid

def main(av):
    if len(av) != 2:
        exit(84)
    else:
        grid = init_grid(av[1])
        while not empty_grid(grid):
            print_grid(grid)
            grid = game_of_life(grid)
            time.sleep(1)
            os.system("clear")
        print_grid(grid)

if __name__ == '__main__':
    main(sys.argv)