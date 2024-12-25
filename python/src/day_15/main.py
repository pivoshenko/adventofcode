"""Day 15: Warehouse Woes.

https://adventofcode.com/2024/day/15
"""

from __future__ import annotations

from pathlib import Path


cwd = Path(__file__).parent


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


def run_part_1(
    warehouse: list[list[str]],
    moves: str,
    directions: dict[str, tuple[int, int]],
) -> int:
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


def run(input_data: str) -> tuple[int, int]:
    warehouse_str, moves = input_data.strip().split("\n\n")

    warehouse = [list(line) for line in warehouse_str.strip().split("\n")]
    moves = moves.replace("\n", "")

    directions = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }

    part_1_answer = run_part_1(warehouse, moves, directions)
    part_2_answer = 0
    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 2028
    expected_part_2_answer = 0

    with (cwd / "example.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expected_part_2_answer)


if __name__ == "__main__":
    with (cwd / "input.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)
    print(part_1_answer, part_2_answer)
