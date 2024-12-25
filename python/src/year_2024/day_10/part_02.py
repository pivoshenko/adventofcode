"""Day 10: Hoof It (#2).

https://adventofcode.com/2024/day/10
"""

from __future__ import annotations

import pathlib
import argparse
import collections

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from collections.abc import Iterator


peak = 9


def get_neighbors(x: int, y: int, grid: list[list[int]]) -> Iterator[tuple[int, int]]:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    height = len(grid)
    width = len(grid[0])

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < width and 0 <= new_y < height:
            yield (new_x, new_y)


def count_distinct_trails(start: tuple[int, int], grid: list[list[int]]) -> int:
    distinct_paths = set()
    queue = collections.deque([(start, (start,))])

    while queue:
        (x, y), path = queue.popleft()
        current_height = grid[y][x]

        if current_height == peak:
            distinct_paths.add(path)
            continue

        for nx, ny in get_neighbors(x, y, grid):
            next_pos = (nx, ny)
            if next_pos in path:
                continue

            next_height = grid[ny][nx]
            if next_height == current_height + 1:
                new_path = (*path, next_pos)
                queue.append((next_pos, new_path))  # type: ignore[arg-type]

    return len(distinct_paths)


def run(input_data: str) -> int:
    grid = [list(map(int, line.strip())) for line in input_data.splitlines() if line.strip()]

    trailheads: list[tuple[int, int]] = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                trailheads.append((x, y))  # noqa: PERF401

    return sum(count_distinct_trails(trailhead, grid) for trailhead in trailheads)


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 81

    with (examples_dir / "day_10.txt").open() as file:
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
