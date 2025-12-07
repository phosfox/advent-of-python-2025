from pathlib import Path

import numpy as np
from numpy._typing import NDArray


def parse(input) -> NDArray:
    lines = Path(input).read_text().strip().splitlines()
    grid = [list(line) for line in lines]
    grid = np.array(grid, dtype=str)
    return grid


def part1():
    grid = parse("inputs/day07_test.txt")
    print(np.sum(grid == "^"))
    width, height = grid.shape
    split = 0
    for (x, y), ele in np.ndenumerate(grid):
        front = (x + 1, y)
        front_left = (x + 1, y - 1)
        front_right = (x + 1, y + 1)
        if x == height or y == width - 1:
            continue
        if ele == "S":
            grid[front] = "|"
        if ele == "|" and grid[front] == "^":
            split += 1
            if grid[front_left] == ".":
                grid[front_left] = "|"
            if grid[front_right] == ".":
                grid[front_right] = "|"
        if ele == "|" and grid[front] != "^":
            grid[front] = "|"

    print(grid)
    print(np.argwhere(grid == "|"))
    print("amount of |", np.sum(grid == "|"))
    print("amount of ^", np.sum(grid == "^"))
    print(split)
    pass


def part2():
    grid = parse("inputs/day07.txt")
    splitters = np.sum(grid == "^")
    width, height = grid.shape
    split = 0
    paths = set()
    for (x, y), ele in np.ndenumerate(grid):
        front = (x + 1, y)
        front_left = (x + 1, y - 1)
        front_right = (x + 1, y + 1)
        if x == height or y == width - 1:
            continue
        if ele == "S":
            grid[front] = "|"
        if ele == "|" and grid[front] == "^":
            if grid[front_left] == ".":
                grid[front_left] = "|"
                split += 1
            if grid[front_right] == ".":
                grid[front_right] = "|"
                split += 1
        if ele == "|" and grid[front] != "^":
            grid[front] = "|"

    available_paths = np.argwhere(grid == "|")
    print(grid)
    last_row_ways = np.sum(grid[height:] == "|")
    print(split)
    print(last_row_ways)
    print(split + last_row_ways - 1)
    pass
