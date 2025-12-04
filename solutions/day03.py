from itertools import combinations
from pathlib import Path
from typing import Iterable

from day_base import SolutionBase


def parse_bank(bank):
    return [int(b) for b in bank]


def parse(input):
    lines = Path(input).read_text().splitlines()
    banks = [list(line) for line in lines]
    return [parse_bank(bank) for bank in banks]


def joltage(bank):
    largest = -1
    largest_idx = -1
    second_largest = -1
    for idx, battery in enumerate(bank):
        if idx == len(bank) - 1:
            continue
        if battery > largest:
            largest = battery
            largest_idx = idx

    for idx, battery in enumerate(bank):
        if battery > second_largest and idx > largest_idx:
            second_largest = battery
    return int(str(largest) + str(second_largest))


def bank_to_number(bank: Iterable[int]):
    return int("".join(map(str, bank)))


def max_combination(bank):
    m = max(bank_to_number(b) for b in combinations(bank, len(bank) - 1))
    return [int(s) for s in str(m)]


def joltage2(bank: list[int]):
    while len(bank) > 12:
        max_comb = max_combination(bank)
        bank = max_comb
    return bank_to_number(bank)


class Day03(SolutionBase):
    def part1(self):
        banks = parse("inputs/day03.txt")
        joltages = [joltage(bank) for bank in banks]
        print(sum(joltages))

    def part2(self):
        banks = parse("inputs/day03.txt")
        joltages = [joltage2(bank) for bank in banks]
        print(sum(joltages))
