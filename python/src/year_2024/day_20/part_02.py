"""Day 20: Race Condition (#2).

https://adventofcode.com/2024/day/20
"""

from __future__ import annotations

import pathlib
import argparse
import collections


def find_start(maze: list[list[str]]) -> tuple[int, int]:
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == "S":
                return y, x
    return -1, -1


def inbounds(position: tuple[int, int], rows: int, columns: int) -> bool:
    return 0 <= position[0] < rows and 0 <= position[1] < columns


def get_neighbours(
    maze: list[list[str]],
    positionition: tuple[int, int],
    rows: int,
    columns: int,
) -> list[tuple[int, int]]:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    neighbours = []
    for direction in directions:
        new_positionition = positionition[0] + direction[0], positionition[1] + direction[1]
        if (
            inbounds(new_positionition, rows, columns)
            and maze[new_positionition[0]][new_positionition[1]] != "#"
        ):
            neighbours.append(new_positionition)
    return neighbours


def bfs(
    maze: list[list[str]],
    start: tuple[int, int],
) -> tuple[dict[tuple[int, int], int], list[tuple[int, int]]]:
    rows, columns = len(maze), len(maze[0])
    distances = {start: 0}
    queue = collections.deque([(0, start)])
    path = []

    while queue:
        distance, positionition = queue.popleft()
        path.append(positionition)
        for next_positionition in get_neighbours(maze, positionition, rows, columns):
            if next_positionition not in distances:
                distances[next_positionition] = distance + 1
                queue.append((distance + 1, next_positionition))

    return distances, path


def run(input_data: str) -> int:
    maze = [list(line) for line in input_data.strip().split("\n")]
    start = find_start(maze)
    distances, path = bfs(maze, start)

    max_delta = 20

    rev_path = path[::-1]
    cost = 0

    for y in range(len(rev_path)):
        for x in range(y + 1, len(rev_path)):
            position_1, position_2 = rev_path[y], rev_path[x]
            delta = abs(position_1[0] - position_2[0]) + abs(position_1[1] - position_2[1])
            if delta <= max_delta:
                new_cost = distances[position_1] - distances[position_2] - delta
                if new_cost >= 100:
                    cost += 1

    return cost


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 0

    with (examples_dir / "day_20.txt").open() as file:
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
