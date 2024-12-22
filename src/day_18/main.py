"""Day 18: RAM Run.

https://adventofcode.com/2024/day/18
"""

from __future__ import annotations

import heapq

from pathlib import Path


cwd = Path(__file__).parent


def run_part_1(falling_bytes: list[tuple[int, ...]]) -> int:
    width = 71
    height = 71

    grid = [["."] * width for _ in range(height)]
    for falling_byte in falling_bytes:
        x, y = falling_byte
        grid[y][x] = "#"

    moves = [(0, 0, 0)]
    seen = set()
    while moves:
        steps, x, y = heapq.heappop(moves)

        if (x, y) == (70, 70):
            return steps

        if (x, y) in seen:
            continue
        seen.add((x, y))

        for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
            if not 0 <= nx < width or not 0 <= ny < height:
                continue
            if grid[ny][nx] == "#":
                continue

            heapq.heappush(moves, (steps + 1, nx, ny))

    return -1


def run(input_data: str) -> tuple[int, int]:
    falling_bytes = [tuple(map(int, line.split(","))) for line in input_data.strip().split("\n")]

    part_1_answer = run_part_1(falling_bytes)
    part_2_answer = 0

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 146
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
