import math
from dataclasses import dataclass
from itertools import combinations
from pathlib import Path

import numpy as np


@dataclass
class Point:
    x: int
    y: int
    z: int

    def __eq__(self, other: object, /) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))


def parse(input) -> list[Point]:
    lines: list[str] = Path(input).read_text().splitlines()
    boxes = []
    for line in lines:
        ps = [int(p) for p in line.split(",")]
        boxes.append(Point(ps[0], ps[1], ps[2]))
    return boxes


def distance(a: Point, b: Point):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2)


def remove(a, b, circuits):
    if set([b]) in circuits:
        circuits.remove(set([b]))
    if set([a]) in circuits:
        circuits.remove(set([a]))


def part1():
    boxes = parse("inputs/day08_test.txt")
    circuits: list[set] = [set([p]) for p in boxes]
    distances = []

    for a, b in combinations(boxes, 2):
        dist = distance(a, b)
        distances.append((dist, (a, b)))

    connections = 0
    for _, (a, b) in sorted(distances, key=lambda t: t[0])[:10]:
        if circuits[a] != circuits[b]:
            new = circuits[a] | circuits[b]
            for c in new:
                circuits[c] = new
            print("new", new)
            pass
    print(sorted(list(map(len, circuits.values())), reverse=True))
    print(np.prod(sorted(list(map(len, circuits.values())), reverse=True)[:3]))
    pprint.pp(circuits)


def part2():
    pass
