"""Day 16: Reindeer Maze (#1).

https://adventofcode.com/2024/day/16
"""

from __future__ import annotations

import heapq
import pathlib
import argparse


def find_start_and_end(maze: list[list[str]]) -> tuple[tuple[int, int], tuple[int, int]]:
    for x, row in enumerate(maze):
        for y, tile in enumerate(row):
            if tile == "S":
                start = (x, y)
            elif tile == "E":
                end = (x, y)
    return start, end


def is_valid_move(maze: list[list[str]], x: int, y: int) -> bool:
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != "#"


def run(input_data: str) -> int:
    maze = [list(line) for line in input_data.strip().splitlines()]

    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]

    start, end = find_start_and_end(maze)

    pq = [(0, start[0], start[1], 0)]
    heapq.heapify(pq)
    visited = set()

    while pq:
        cost, x, y, dir_ = heapq.heappop(pq)
        if (x, y) == end:
            return cost

        if (x, y, dir_) in visited:
            continue

        visited.add((x, y, dir_))

        nx, ny = x + directions[dir_][0], y + directions[dir_][1]
        if is_valid_move(maze, nx, ny):
            heapq.heappush(pq, (cost + 1, nx, ny, dir_))

        for rotation in [-1, 1]:
            new_dir = (dir_ + rotation) % 4
            heapq.heappush(pq, (cost + 1000, x, y, new_dir))

    return -1


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 7036

    with (examples_dir / "day_16.txt").open() as file:
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
