"""Day 8: Resonant Collinearity.

https://adventofcode.com/2024/day/8
"""

from __future__ import annotations

import itertools
import collections

from pathlib import Path


cwd = Path(__file__).parent


def find_antinodes(
    grid: set[tuple[int, int]],
    antennas: list[tuple[int, int]],
) -> set[tuple[int, int]]:
    return grid & {
        (2 * row - row_other, 2 * col - col_other)
        for (row, col), (row_other, col_other) in itertools.permutations(antennas, r=2)
    }


def find_all_antinodes(
    grid: set[tuple[int, int]],
    antennas: list[tuple[int, int]],
) -> set[tuple[int, int]]:
    antinodes = set()
    for (row, col), (row_other, col_other) in itertools.permutations(antennas, r=2):
        dr, dc = row_other - row, col_other - col
        for n in itertools.count(1):
            if (antinode := (row + n * dr, col + n * dc)) not in grid:
                break
            antinodes.add(antinode)
    return antinodes


def run(input_data: str) -> tuple[int, int]:
    unpar_grid = {
        (row, col): char
        for row, line in enumerate(input_data.split("\n"))
        for col, char in enumerate(line)
    }
    grid = set(unpar_grid)

    antennas = collections.defaultdict(list)
    for pos, char in unpar_grid.items():
        if char != ".":
            antennas[char].append(pos)

    # part 1
    antinodes = [find_antinodes(grid, pos) for pos in antennas.values()]
    common = set.union(*antinodes)
    part_1_answer = len(common)

    # part 2
    all_antinodes = [find_all_antinodes(grid, pos) for pos in antennas.values()]
    common = set.union(*all_antinodes)
    part_2_answer = len(common)

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 14
    expectd_part_2_answer = 34

    with (cwd / "example.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expectd_part_2_answer)


if __name__ == "__main__":
    with (cwd / "input.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)
    print(part_1_answer, part_2_answer)
