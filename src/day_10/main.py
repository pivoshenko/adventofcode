"""Day 10: Hoof It.

https://adventofcode.com/2024/day/10
"""

from __future__ import annotations

from collections import deque
from pathlib import Path
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from collections.abc import Iterator


cwd = Path(__file__).parent


def get_neighbors(x: int, y: int, grid: list[list[int]]) -> Iterator[tuple[int, int]]:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    height = len(grid)
    width = len(grid[0])

    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < width and 0 <= new_y < height:
            yield (new_x, new_y)


def count_reachable_nines(start: tuple[int, int], grid: list[list[int]]) -> int:
    visited = set()
    reachable_nines = set()
    queue = deque([(start, {start})])

    while queue:
        (x, y), path = queue.popleft()
        current_height = grid[y][x]

        if current_height == 9:  # noqa: PLR2004
            reachable_nines.add((x, y))
            continue

        for nx, ny in get_neighbors(x, y, grid):
            next_pos = (nx, ny)
            if next_pos in path:
                continue

            next_height = grid[ny][nx]
            if next_height == current_height + 1:
                new_path = path | {next_pos}
                state = (next_pos, frozenset(new_path))
                if state not in visited:
                    visited.add(state)
                    queue.append((next_pos, new_path))

    return len(reachable_nines)


def count_distinct_trails(start: tuple[int, int], grid: list[list[int]]) -> int:
    distinct_paths = set()
    queue = deque([(start, (start,))])

    while queue:
        (x, y), path = queue.popleft()
        current_height = grid[y][x]

        if current_height == 9:  # noqa: PLR2004
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


def run(path_to_input_data: Path) -> tuple[int, ...]:
    with path_to_input_data.open("r") as file:
        grid = [[int(char) for char in line.strip()] for line in file if line.strip()]

    trailheads: list[tuple[int, int]] = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                trailheads.append((x, y))  # noqa: PERF401

    part_1_answer = sum(count_reachable_nines(trailhead, grid) for trailhead in trailheads)

    part_2_answer = sum(count_distinct_trails(trailhead, grid) for trailhead in trailheads)

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 36
    expectd_part_2_answer = 81

    part_1_answer, part_2_answer = run(cwd / "example.txt")

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expectd_part_2_answer)


if __name__ == "__main__":
    part_1_answer, part_2_answer = run(cwd / "input.txt")
    print(part_1_answer, part_2_answer)
