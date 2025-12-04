from pathlib import Path

import numpy as np
from numpy._typing import NDArray


def parse(input) -> NDArray:
    lines = Path(input).read_text().splitlines()
    grid = [list(line) for line in lines]
    grid = np.array(grid, dtype=str)
    return grid


#  abc
#  dXe
#  fgh
def neighbour_indices(x, y, shape) -> list[tuple[int, int]]:
    points = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    nb_indices = []
    (width, height) = shape
    for nb_x, nb_y in points:
        x_idx = x + nb_x
        y_idx = y + nb_y
        if x_idx < 0 or y_idx < 0 or x_idx >= width or y_idx >= height:
            continue
        nb_indices.append((x_idx, y_idx))
    return nb_indices


def neighbours(nb_indices: list[tuple[int, int]], grid: NDArray) -> NDArray:
    nbs = []
    for x, y in nb_indices:
        nbs.append(grid[x, y])
    return np.array(nbs)


def find_removable_rolls(grid) -> list[tuple[int, int]]:
    removable_rolls = []
    for (x, y), ele in np.ndenumerate(grid):
        if ele != "@":
            continue
        nb_indices = neighbour_indices(x, y, grid.shape)
        nbs = neighbours(nb_indices, grid)
        if np.sum(nbs == "@") < 4:
            removable_rolls.append((x, y))
    return removable_rolls


def part1():
    grid = parse("inputs/day04.txt")
    removable_rolls = find_removable_rolls(grid)
    print(len(removable_rolls))


def part2():
    grid = parse("inputs/day04.txt")
    total_rolls_removed = 0
    while True:
        removable_rolls = find_removable_rolls(grid)
        amount_of_removable_rolls = len(removable_rolls)
        if (total_rolls_removed + amount_of_removable_rolls) == total_rolls_removed:
            break
        total_rolls_removed += amount_of_removable_rolls
        for x, y in removable_rolls:
            grid[x, y] = "X"
    print(total_rolls_removed)
