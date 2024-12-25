"""Day 18: RAM Run (#1).

https://adventofcode.com/2024/day/18
"""

from __future__ import annotations

import heapq
import pathlib
import argparse


def run(input_data: str) -> int:
    falling_bytes = [tuple(map(int, line.split(","))) for line in input_data.strip().split("\n")]

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


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 146

    with (examples_dir / "day_18.txt").open() as file:
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
