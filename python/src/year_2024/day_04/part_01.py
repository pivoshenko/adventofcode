"""Day 4: Ceres Search (#1).

https://adventofcode.com/2024/day/4
"""

from __future__ import annotations

import pathlib
import argparse


def run(input_data: str) -> int:
    grid = input_data.splitlines()
    rows = len(grid)
    columns = len(grid[0])

    keyword = "XMAS"
    keyword_len = len(keyword)

    directions = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (1, 1),
        (-1, -1),
        (1, -1),
        (-1, 1),
    ]

    def is_valid(x: int, y: int) -> bool:
        return 0 <= x < rows and 0 <= y < columns

    def search_from(x: int, y: int, dx: int, dy: int) -> bool:
        for i in range(keyword_len):
            new_x, new_y = x + i * dx, y + i * dy
            if not is_valid(new_x, new_y) or grid[new_x][new_y] != keyword[i]:
                return False
        return True

    keyword_occurrences = 0
    for starting_pos_x in range(rows):
        for starting_pos_y in range(columns):
            if grid[starting_pos_x][starting_pos_y] == keyword[0]:
                for dx, dy in directions:
                    if search_from(starting_pos_x, starting_pos_y, dx, dy):
                        keyword_occurrences += 1

    return keyword_occurrences


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 18

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
