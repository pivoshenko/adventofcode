"""Day 14: Restroom Redoubt (#1).

https://adventofcode.com/2024/day/14
"""

from __future__ import annotations

import re
import pathlib
import argparse


def parse_robot_params(robot: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", robot)))


def run(input_data: str, width: int, height: int) -> int:
    robots_params = [parse_robot_params(robot) for robot in input_data.splitlines()]

    num_seconds = 100

    updated_positions = []
    for robot_params in robots_params:
        x, y, dx, dy = robot_params
        new_x = (x + num_seconds * dx) % width
        new_y = (y + num_seconds * dy) % height
        updated_positions.append((new_x, new_y))

    quadrant_counts = [0, 0, 0, 0]
    for x, y in updated_positions:
        if x < width // 2 and y < height // 2:
            quadrant_counts[0] += 1
        elif x > width // 2 and y < height // 2:
            quadrant_counts[1] += 1
        elif x < width // 2 and y > height // 2:
            quadrant_counts[2] += 1
        elif x > width // 2 and y > height // 2:
            quadrant_counts[3] += 1

    return quadrant_counts[0] * quadrant_counts[1] * quadrant_counts[2] * quadrant_counts[3]


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 12

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
