"""Day 8: Resonant Collinearity (#2).

https://adventofcode.com/2024/day/8
"""

from __future__ import annotations

import pathlib
import argparse
import itertools
import collections


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


def run(input_data: str) -> int:
    grid_section = {
        (row, col): char
        for row, line in enumerate(input_data.split("\n"))
        for col, char in enumerate(line)
    }
    grid = set(grid_section)

    antennas = collections.defaultdict(list)
    for position, char in grid_section.items():
        if char != ".":
            antennas[char].append(position)

    all_antinodes = [find_all_antinodes(grid, position) for position in antennas.values()]
    common = set.union(*all_antinodes)
    return len(common)


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 34

    with (examples_dir / "day_08.txt").open() as file:
        input_data = file.read()

    answer = run(input_data)
    assert answer == expected_answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-f",
        "--filepath",
        dest="filepath",
        type=pathlib.Path,
        required=True,
    )
    args = parser.parse_args()

    with args.filepath.open() as file:
        input_data = file.read()

    answer = run(input_data)
    print(answer)
