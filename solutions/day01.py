import re
from dataclasses import dataclass
from itertools import accumulate

from day_base import SolutionBase


def parse(input):
    rotations = []
    with open(input) as f:
        lines = f.readlines()
        for line in lines:
            pattern = "(L|R)(\\d+)"
            match = re.search(pattern, line)
            if match is None:
                return rotations
            direction = match.group(1)
            distance = int(match.group(2))
            if direction == "L":
                rotations.append(-distance)
            else:
                rotations.append(distance)
    return rotations


def rotate(position, rotation):
    return (position + rotation) % 100


def clicks(position, rotation):
    inc = -1 if rotation < 0 else 1
    nextPosition = position
    rotations = abs(rotation)
    zero_clicks = 0
    for i in range(rotations):
        nextPosition = (nextPosition + inc) % 100
        if nextPosition == 0 and i < rotations - 1:
            zero_clicks += 1
    return zero_clicks


def rotate_with_zero_clicks(step: Step, rotation):
    newPosition = rotate(step.position, rotation)
    zero_clicks = clicks(step.position, rotation)
    newStep = Step(newPosition, zero_clicks)
    print(step.position, "Ne", newStep, rotation)
    return newStep


@dataclass
class Step:
    position: int
    zero_clicks: int


class Day01(SolutionBase):
    def part1(self):
        starting_point = 50
        rotations = parse("inputs/day01.txt")
        steps = accumulate(rotations, rotate, initial=starting_point)
        zeroes = list(steps).count(0)
        return print(zeroes)

    def part2(self):
        starting_point = 50
        rotations = parse("inputs/day01.txt")
        steps = accumulate(rotations, rotate, initial=starting_point)
        zeroes = list(steps).count(0)
        initial = Step(50, 0)
        steps_with_any_zero_clicks = accumulate(
            rotations, rotate_with_zero_clicks, initial=initial
        )
        zero_clicks = sum(step.zero_clicks for step in steps_with_any_zero_clicks)
        print(zero_clicks + zeroes)
