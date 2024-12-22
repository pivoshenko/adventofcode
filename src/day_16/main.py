"""Day 16: Reindeer Maze.

https://adventofcode.com/2024/day/16
"""

from __future__ import annotations

import heapq

from pathlib import Path


cwd = Path(__file__).parent


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


def run_part_1(maze: list[list[str]]) -> int:
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


def run(input_data: str) -> tuple[int, int]:
    maze = [list(line) for line in input_data.strip().splitlines()]

    part_1_answer = run_part_1(maze)
    part_2_answer = 0

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 7036
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
