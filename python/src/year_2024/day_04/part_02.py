"""Day 4: Ceres Search (#2).

https://adventofcode.com/2024/day/4
"""

from __future__ import annotations

import pathlib
import argparse


def run(input_data: str) -> int:
    grid = input_data.splitlines()
    rows = len(grid)
    columns = len(grid[0])

    keyword_set = {"M", "S"}

    keyword_occurrences = 0
    for starting_pos_x in range(1, rows - 1):
        for starting_pos_y in range(1, columns - 1):
            if grid[starting_pos_x][starting_pos_y] == "A":  # noqa: SIM102
                if {
                    grid[starting_pos_x - 1][starting_pos_y - 1],
                    grid[starting_pos_x + 1][starting_pos_y + 1],
                } == keyword_set and {
                    grid[starting_pos_x - 1][starting_pos_y + 1],
                    grid[starting_pos_x + 1][starting_pos_y - 1],
                } == keyword_set:
                    keyword_occurrences += 1

    return keyword_occurrences


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 9

    with (examples_dir / "day_04.txt").open() as file:
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
