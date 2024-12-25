"""Day 15: Warehouse Woes (#1).

https://adventofcode.com/2024/day/15
"""

from __future__ import annotations

import pathlib
import argparse


def find_robot_position(warehouse: list[list[str]]) -> tuple[int, int]:
    for y, row in enumerate(warehouse):
        for x, cell in enumerate(row):
            if cell == "@":
                return y, x
    return -1, -1


def gps(warehouse: list[list[str]]) -> int:
    distance = 0
    rows, columns = len(warehouse), len(warehouse[0])
    for y in range(rows):
        for x in range(columns):
            if warehouse[y][x] == "O":
                distance += 100 * y + x
    return distance


def run(input_data: str) -> int:
    warehouse_str, moves = input_data.strip().split("\n\n")

    warehouse = [list(line) for line in warehouse_str.strip().split("\n")]
    moves = moves.replace("\n", "")

    directions = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }

    for move in moves:
        robot_position = find_robot_position(warehouse)
        dy, dx = directions[move]

        y, x = robot_position[0] + dy, robot_position[1] + dx

        can_move = False
        while warehouse[y][x] != "#":
            if warehouse[y][x] == ".":
                can_move = True
                break
            y += dy
            x += dx

        if can_move:
            y, x = robot_position[0] + dy, robot_position[1] + dx
            while warehouse[y][x] == "O":
                y += dy
                x += dx

            warehouse[y][x] = "O"
            warehouse[robot_position[0]][robot_position[1]] = "."
            warehouse[robot_position[0] + dy][robot_position[1] + dx] = "@"

    return gps(warehouse)


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 2028

    with (examples_dir / "day_15.txt").open() as file:
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
