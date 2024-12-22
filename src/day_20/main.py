"""Day 20: RAcolumns Run.

https://adventofcode.com/2024/day/18
"""

from __future__ import annotations

from collections import deque
from pathlib import Path


cwd = Path(__file__).parent


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


def get_two_step_neighbours(
    maze: list[list[str]],
    position: tuple[int, int],
    rows: int,
    columns: int,
) -> list[tuple[int, int]]:
    two_step_dirs = [(0, 2), (0, -2), (2, 0), (-2, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    neighbours = []
    for direction in two_step_dirs:
        new_positionition = position[0] + direction[0], position[1] + direction[1]
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
    queue = deque([(0, start)])
    path = []

    while queue:
        distance, positionition = queue.popleft()
        path.append(positionition)
        for next_positionition in get_neighbours(maze, positionition, rows, columns):
            if next_positionition not in distances:
                distances[next_positionition] = distance + 1
                queue.append((distance + 1, next_positionition))

    return distances, path


def run_part_1(
    path: list[tuple[int, int]],
    distances: dict[tuple[int, int], int],
    maze: list[list[str]],
) -> int:
    rows, columns = len(maze), len(maze[0])
    answer = 0
    for position in path[::-1]:
        neighbours = get_two_step_neighbours(maze, position, rows, columns)
        for neighbour in neighbours:
            new_cost = distances[position] - distances[neighbour] - 2
            if new_cost >= 100:
                answer += 1
    return answer


def run_part_2(
    path: list[tuple[int, int]],
    distances: dict[tuple[int, int], int],
    max_delta: int,
) -> int:
    path_rev = path[::-1]
    answer = 0
    for y in range(len(path_rev)):
        for x in range(y + 1, len(path_rev)):
            position_1, position_2 = path_rev[y], path_rev[x]
            delta = abs(position_1[0] - position_2[0]) + abs(position_1[1] - position_2[1])
            if delta <= max_delta:
                new_cost = distances[position_1] - distances[position_2] - delta
                if new_cost >= 100:
                    answer += 1

    return answer


def run(input_data: str) -> tuple[int, int]:
    maze = [list(line) for line in input_data.strip().split("\n")]
    start = find_start(maze)
    distances, path = bfs(maze, start)

    part_1_answer = run_part_1(path, distances, maze)
    part_2_answer = run_part_2(path, distances, 20)

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 1355
    expected_part_2_answer = 1007335

    with (cwd / "input.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expected_part_2_answer)


if __name__ == "__main__":
    with (cwd / "input.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)
    print(part_1_answer, part_2_answer)
