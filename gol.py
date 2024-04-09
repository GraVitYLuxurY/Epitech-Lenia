import sys

cell_char = '#'
check_around = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]

def init_grid(file):
    with open(file) as f:
        return [[i for i in list(line)] for line in f]

def empty_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == cell_char:
                return False
    return True

def can_live(cell):
    cells_around = 0
    for pos in check_around:
        try:
            if cell[pos[0]][pos[1]] == cell_char:
                cells_around += 1
        except:
            pass
    if (cells_around < 2 or cells_around > 3) and cell == cell_char:
        return '.'
    elif cells_around == 3 and cell == '.':
        return cell_char
    elif cells_around == 2 and cell == cell_char:
        return cell_char
    else:
        return '.'

def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')

def game_of_life(grid):
    new_grid = grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            new_grid[i][j] = can_live(grid[i][j])
    return new_grid

def main(av):
    if len(av) != 2:
        exit(84)
    else:
        grid = init_grid(av[1])
        while not empty_grid(grid):
            print_grid(grid)
            grid = game_of_life(grid)

if __name__ == '__main__':
    main(sys.argv)