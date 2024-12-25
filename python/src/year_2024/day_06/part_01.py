"""Day 6: Guard Gallivant (#1).

https://adventofcode.com/2024/day/6
"""

from __future__ import annotations

import pathlib
import argparse


def count_visited_tiles(grid: list[list[str]], tile: str, obstacle: str) -> int:
    return sum(1 for row in grid for cell in row if cell not in (tile, obstacle))


def find_guard(grid: list[list[str]], tile: str, obstacle: str) -> tuple[int, int, str]:
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell not in (tile, obstacle):
                return x, y, cell
    return -1, -1, ""


def move_guard(  # noqa: PLR0913
    curr_guard_pos_x: int,
    curr_guard_pos_y: int,
    curr_guard_dir: str,
    grid: list[list[str]],
    directions: dict[str, tuple[int, int]],
    obstacle: str,
    visited: str,
) -> None:
    guard_up, guard_right, guard_down, guard_left = directions.keys()
    while True:
        dir_x, dir_y = directions[curr_guard_dir]
        new_guard_pos_x = curr_guard_pos_x + dir_x
        new_guard_pos_y = curr_guard_pos_y + dir_y
        if grid[new_guard_pos_y][new_guard_pos_x] != obstacle:
            grid[new_guard_pos_y][new_guard_pos_x] = curr_guard_dir
            grid[curr_guard_pos_y][curr_guard_pos_x] = visited
            curr_guard_pos_x, curr_guard_pos_y = new_guard_pos_x, new_guard_pos_y
        else:
            curr_guard_dir = {
                guard_up: guard_right,
                guard_right: guard_down,
                guard_down: guard_left,
                guard_left: guard_up,
            }[curr_guard_dir]


def run(input_data: str) -> int:
    grid = [list(line) for line in input_data.splitlines()]

    tile, obstacle, visited = ".", "#", "X"
    directions = {
        "^": (0, -1),
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
    }
    curr_guard_pos_x, curr_guard_pos_y, curr_guard_dir = find_guard(grid, tile, obstacle)
    try:
        move_guard(
            curr_guard_pos_x,
            curr_guard_pos_y,
            curr_guard_dir,
            grid,
            directions,
            obstacle,
            visited,
        )
    except IndexError:
        return count_visited_tiles(grid, tile, obstacle)

    return -1


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 41

    with (examples_dir / "day_06.txt").open() as file:
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
