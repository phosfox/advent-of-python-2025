from pathlib import Path

from day_base import SolutionBase


def parse(input) -> list[list[int]]:
    ranges: list[list[int]] = []
    for r in Path(input).read_text().strip().split(","):
        start, end = r.split("-")
        ranges.append([int(start), int(end)])
    return ranges


def expand_range(id_range):
    start, end = id_range
    return [x for x in range(start, end + 1)]


def is_invalid(id) -> bool:
    str_id = str(id)
    if len(str_id) % 2 != 0:
        return False
    half = len(str_id) // 2
    left = str_id[:half]
    right = str_id[half:]
    return left == right


def is_invalid2(id) -> bool:
    str_id = str(id)
    str_len = len(str_id)
    first = str_id[0]
    for d in str_id[1:]:
        if first * (str_len // len(first)) == str_id:
            return True
        first += d
    return False


class Day02(SolutionBase):
    def part1(self):
        ranges = parse("inputs/day02.txt")
        invalid_sum = 0
        for id_range in ranges:
            expanded_range = expand_range(id_range)
            for id in expanded_range:
                if is_invalid(id):
                    invalid_sum += id
        print(invalid_sum)

    def part2(self):
        ranges = parse("inputs/day02.txt")
        invalid_sum = 0
        for id_range in ranges:
            expanded_range = expand_range(id_range)
            for id in expanded_range:
                if is_invalid2(id):
                    invalid_sum += id
        print(invalid_sum)
