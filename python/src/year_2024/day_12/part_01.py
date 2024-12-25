"""Day 12: Garden Groups (#1).

https://adventofcode.com/2024/day/12
"""

from __future__ import annotations

import pathlib
import argparse
import collections


def run(input_data: str) -> int:
    grid = [list(row) for row in input_data.splitlines()]

    def bfs(start: tuple[int, int], plant_type: str) -> tuple[int, int]:
        queue = collections.deque([start])
        visited.add(start)
        area = 0
        perimeter = 0
        while queue:
            x, y = queue.popleft()
            area += 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < columns and grid[nx][ny] == plant_type:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                else:
                    perimeter += 1
        return area, perimeter

    rows: int = len(grid)
    columns: int = len(grid[0])
    visited: set[tuple[int, int]] = set()
    total_cost: int = 0

    for y in range(rows):
        for x in range(columns):
            if (y, x) not in visited:
                plant_type = grid[y][x]
                area, perimeter = bfs((y, x), plant_type)
                total_cost += area * perimeter

    return total_cost


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 1930

    with (examples_dir / "day_12.txt").open() as file:
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
