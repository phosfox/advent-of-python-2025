from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from numpy._core.numeric import argwhere
from numpy._typing import NDArray


def parse(input) -> NDArray:
    lines = Path(input).read_text().strip().splitlines()
    grid = [list(line) for line in lines]
    grid = np.array(grid, dtype=str)
    return grid


def parse2(input) -> list[str]:
    lines = Path(input).read_text().strip().splitlines()
    return lines


def grid_with_paths(grid):
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
    return (grid, split)


def part1():
    print("part 1")
    grid, split = grid_with_paths(parse("inputs/day07_test.txt"))
    print(grid)
    print(split)
    pass


def delete_beam(beams: list, beam: int):
    if beam in beams:
        beams.remove(beam)


def part2():
    print("part 2")
    grid, split = grid_with_paths(parse("inputs/day07_test.txt"))
    print(grid)
    (x, y) = np.argwhere(grid == "S")[0]
    bs = defaultdict(int)
    bs[int(y)] = 1
    for (x, y), ele in np.ndenumerate(grid):
        if ele == "^" and grid[x - 1, y] == "|":
            print(bs)
            paths = bs[y]
            bs[y] -= paths
            bs[y-1] += paths
            bs[y+1] += paths
    print(sum(bs.values()))
    print(bs.values())
