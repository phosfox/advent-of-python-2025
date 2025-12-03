import sys
from collections import deque
from itertools import batched, islice
from operator import pos
from pathlib import Path
from sqlite3 import SQLITE_OK_LOAD_PERMANENTLY
from syslog import LOG_WARNING

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
    second_largest_idx = -1
    for idx, battery in enumerate(bank):
        if idx == len(bank) - 1:
            continue
        if battery > largest:
            largest = battery
            largest_idx = idx

    for idx, battery in enumerate(bank):
        if battery > second_largest and idx > largest_idx:
            second_largest = battery
            second_largest_idx = idx
    return int(str(largest) + str(second_largest))


def find_max(bank_slice):
    largest = -1
    largest_idx = -1
    for idx, battery in enumerate(bank_slice):
        if battery > largest:
            largest = battery
            largest_idx = idx
    return (largest, largest_idx)


def joltage2(bank: list[int]):
    print(bank)
    n = 12
    largest_batteries = []
    latest_idx = 0
    for _ in range(n):
        for idx, b in enumerate(bank):
            print(largest_batteries, latest_idx)
            if idx > latest_idx and b > largest_batteries[len(largest_batteries)]:
                largest_batteries.append(b)
                latest_idx = idx

    print(largest_batteries)

    return int("".join(map(str, largest_batteries)))


# 987654321111111
#
def joltage12(bank):
    n = 12
    largest_batteries = []
    windows_size = len(bank) - n
    largest_idx = 0
    for _ in range(n):
        bank_slice = bank[largest_idx:windows_size]
        print(bank_slice)
        largest, largest_idx = find_max(bank_slice)
        largest_batteries.append(largest)
        bank = bank[largest_idx + 1 :]
    return largest_batteries


class Day03(SolutionBase):
    def part1(self):
        banks = parse("inputs/day03.txt")
        joltages = [joltage(bank) for bank in banks]
        print(sum(joltages))

    def part2(self):
        banks = parse("inputs/day03_test.txt")
        joltages = [joltage2(bank) for bank in banks]
        print(joltages)
        print(sum(joltages))
