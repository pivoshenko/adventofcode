"""Day 14: Restroom Redoubt (#2).

https://adventofcode.com/2024/day/14
"""

from __future__ import annotations

import re
import pathlib
import argparse
import collections


def parse_robot_params(robot: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", robot)))


def run(input_data: str, width: int, height: int) -> int:
    robots_params = [parse_robot_params(robot) for robot in input_data.splitlines()]

    num_seconds = width * height

    positions: dict[int, collections.defaultdict[tuple[int, int], int]] = {
        sec: collections.defaultdict(int) for sec in range(num_seconds)
    }
    for robot_params in robots_params:
        x, y, dx, dy = robot_params
        for sec in range(num_seconds):
            new_x = (x + sec * dx) % width
            new_y = (y + sec * dy) % height
            positions[sec][(new_x, new_y)] += 1

    middle_col = (width - 1) / 2
    max_unique_pos_count = 0
    num_easter_eggs = num_seconds
    for sec in range(num_seconds):
        unique_pos_count = 0
        for i in range(-2, 2):
            occupied_col_positions = [
                position for position in positions[sec] if position[1] == middle_col + i
            ]
            unique_pos_count += len(occupied_col_positions)
        if unique_pos_count > max_unique_pos_count:
            max_unique_pos_count = unique_pos_count
            num_easter_eggs = sec

    return num_easter_eggs


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 5

    with (examples_dir / "day_14.txt").open() as file:
        input_data = file.read()

    answer = run(input_data, 11, 7)
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

    answer = run(input_data, 101, 103)
    print(answer)
