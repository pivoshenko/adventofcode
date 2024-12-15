"""Day 12: Garden Groups.

https://adventofcode.com/2024/day/12
"""

from __future__ import annotations

from collections import deque
from pathlib import Path


cwd = Path(__file__).parent


def calculate_fencing_cost(grid: list[list[str]]) -> int:
    def bfs(start: tuple[int, int], plant_type: str) -> tuple[int, int]:
        queue = deque([start])
        visited.add(start)
        area = 0
        perimeter = 0
        while queue:
            x, y = queue.popleft()
            area += 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == plant_type:
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                else:
                    perimeter += 1
        return area, perimeter

    rows: int = len(grid)
    cols: int = len(grid[0])
    visited: set[tuple[int, int]] = set()
    total_cost: int = 0

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                plant_type = grid[i][j]
                area, perimeter = bfs((i, j), plant_type)
                total_cost += area * perimeter

    return total_cost


def calculate_fencing_cost_part_two(grid: list[list[str]]) -> int:
    def bfs(start: tuple[int, int], plant_type: str) -> tuple[int, int]:
        queue = deque([start])
        visited.add(start)
        area = 0
        sides = 0
        while queue:
            x, y = queue.popleft()
            area += 1
            sides += 4  # Each cell starts with 4 sides
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == plant_type:
                    sides -= 1  # Subtract 1 side for each internal connection
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
        return area, sides

    rows: int = len(grid)
    cols: int = len(grid[0])
    visited: set[tuple[int, int]] = set()
    total_cost: int = 0

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in visited:
                plant_type = grid[i][j]
                area, sides = bfs((i, j), plant_type)
                total_cost += area * sides

    return total_cost


def run(input_data: str) -> tuple[int, int]:
    grid = [list(row) for row in input_data.splitlines()]

    part_1_answer = calculate_fencing_cost(grid)

    return part_1_answer, 0


def test_run() -> None:
    expected_part_1_answer = 1930
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
