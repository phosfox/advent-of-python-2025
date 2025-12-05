from itertools import combinations
from pathlib import Path


def parse(input):
    ll = Path(input).read_text().strip().split("\n")
    sep = ll.index("")
    fresh = [tuple(map(int, r.split("-"))) for r in ll[:sep]]

    ingredients = [int(i) for i in ll[sep + 1 :]]

    return fresh, ingredients


def is_fresh(fresh_range, ingredient):
    start, stop = fresh_range
    return ingredient >= start and ingredient <= stop


def is_in_fresh_ids(fresh_ranges, ingredient):
    return any(is_fresh(fresh_range, ingredient) for fresh_range in fresh_ranges)


def part1():
    fresh_ranges, ingredients = parse("inputs/day05.txt")
    fresh_ingredients = []
    for ingredient in ingredients:
        if is_in_fresh_ids(fresh_ranges, ingredient):
            fresh_ingredients.append(ingredient)
    print(len(fresh_ingredients))
    pass


def left_fits_into_right(range_a, range_b):
    start_a, stop_a = range_a
    start_b, stop_b = range_b
    return start_a in range(start_b, stop_b + 1) and stop_a in range(
        start_b, stop_b + 1
    )


def right_fits_into_left(range_a, range_b):
    start_a, stop_a = range_a
    start_b, stop_b = range_b
    return start_b in range(start_a, stop_a + 1) and stop_b in range(
        start_a, stop_a + 1
    )


def left_overlap(range_a, range_b):
    start_a, stop_a = range_a
    start_b, stop_b = range_b
    return start_a <= start_b < stop_a


def right_overlap(range_a, range_b):
    start_a, stop_a = range_a
    start_b, stop_b = range_b
    return start_a < stop_b <= stop_a


def collapse_ranges(fresh_ranges) -> list[list[int]]:
    new_ranges = set()
    used = set()
    for i in range(len(fresh_ranges)):
        for j in range(i + 1, len(fresh_ranges)):
            l, r = fresh_ranges[i], fresh_ranges[j]
            if l in used or r in used:
                break
            if left_fits_into_right(l, r):
                new_ranges.add(r)
                used.add(l)
                used.add(r)
                break
            elif left_overlap(l, r):
                new_ranges.add((l[0], r[1]))
                used.add(l)
                used.add(r)
                break
            elif right_overlap(l, r):
                new_ranges.add((r[0], l[1]))
                used.add(l)
                used.add(r)
                break
        l = fresh_ranges[i]
        if l not in used:
            new_ranges.add(l)
            used.add(fresh_ranges[i])

    return list(new_ranges)


def find_minimum_ranges(fresh_ranges):
    length = len(fresh_ranges)
    while True:
        collapsed = collapse_ranges(fresh_ranges)
        if len(collapsed) == length:
            break
        fresh_ranges = collapsed
        length = len(fresh_ranges)
    return fresh_ranges


def part2():
    fresh_ranges, _ = parse("inputs/day05.txt")
    minimum_ranges = find_minimum_ranges(fresh_ranges)
    print(len(minimum_ranges))
    print(minimum_ranges)
    count = 0
    for start, stop in minimum_ranges[:1]:
        count += len(range(start, stop + 1))
    print(count)
    pass
