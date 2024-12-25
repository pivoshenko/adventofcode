"""Day 14: Restroom Redoubt.

https://adventofcode.com/2024/day/14
"""

from __future__ import annotations

import re

from collections import defaultdict
from pathlib import Path


cwd = Path(__file__).parent


def parse_robot_params(robot: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", robot)))


def run_part_1(robots_params: list[list[int]], width: int, height: int) -> int:
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


def run_part_2(robots_params: list[list[int]], width: int, height: int) -> int:
    num_seconds = width * height

    positions: dict[int, defaultdict[tuple[int, int], int]] = {
        sec: defaultdict(int) for sec in range(num_seconds)
    }
    for robot_params in robots_params:
        x, y, dx, dy = robot_params
        for sec in range(num_seconds):
            new_x = (x + sec * dx) % width
            new_y = (y + sec * dy) % height
            positions[sec][(new_x, new_y)] += 1

    middle_col = (width - 1) / 2
    max_unique_pos_count = 0
    answer = num_seconds
    for sec in range(num_seconds):
        unique_pos_count = 0
        for i in range(-2, 2):
            occupied_col_positions = [pos for pos in positions[sec] if pos[1] == middle_col + i]
            unique_pos_count += len(occupied_col_positions)
        if unique_pos_count > max_unique_pos_count:
            max_unique_pos_count = unique_pos_count
            answer = sec

    return answer


def run(input_data: str, width: int, height: int) -> tuple[int, int]:
    robots_params = [parse_robot_params(robot) for robot in input_data.splitlines()]

    part_1_answer = run_part_1(robots_params, width, height)

    part_2_answer = run_part_2(robots_params, width, height)

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 12
    expected_part_2_answer = 5

    with (cwd / "example.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data, 11, 7)

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expected_part_2_answer)


if __name__ == "__main__":
    with (cwd / "input.txt").open() as file:
        input_data = file.read()

    width = 101
    height = 103

    part_1_answer, part_2_answer = run(input_data, width, height)
    print(part_1_answer, part_2_answer)
