"""Day 4: Ceres Search.

https://adventofcode.com/2024/day/4
"""

from __future__ import annotations

from pathlib import Path


cwd = Path(__file__).parent


def run(input_data: str) -> tuple[int, int]:
    grid = input_data.splitlines()
    rows = len(grid)
    cols = len(grid[0])

    part_1_answer = run_part_1(grid, rows, cols)
    part_2_answer = run_part_2(grid, rows, cols)

    return part_1_answer, part_2_answer


def run_part_1(grid: list[str], rows: int, cols: int) -> int:
    keyword = "XMAS"
    keyword_len = len(keyword)

    directions = [
        (0, 1),  # horizontal right
        (0, -1),  # horizontal left
        (1, 0),  # vertical down
        (-1, 0),  # vertical up
        (1, 1),  # diagonal down-right
        (-1, -1),  # diagonal up-left
        (1, -1),  # diagonal down-left
        (-1, 1),  # diagonal up-right
    ]

    def is_valid(x: int, y: int) -> bool:
        return 0 <= x < rows and 0 <= y < cols

    def search_from(x: int, y: int, dx: int, dy: int) -> bool:
        for i in range(keyword_len):
            new_x, new_y = x + i * dx, y + i * dy
            if not is_valid(new_x, new_y) or grid[new_x][new_y] != keyword[i]:
                return False
        return True

    answer = 0
    for starting_pos_x in range(rows):
        for starting_pos_y in range(cols):
            if grid[starting_pos_x][starting_pos_y] == keyword[0]:
                for dx, dy in directions:
                    if search_from(starting_pos_x, starting_pos_y, dx, dy):
                        answer += 1

    return answer


def run_part_2(grid: list[str], rows: int, cols: int) -> int:
    keyword_set = {"M", "S"}

    answer = 0
    for starting_pos_x in range(1, rows - 1):
        for starting_pos_y in range(1, cols - 1):
            if grid[starting_pos_x][starting_pos_y] == "A":  # noqa: SIM102
                if {
                    grid[starting_pos_x - 1][starting_pos_y - 1],
                    grid[starting_pos_x + 1][starting_pos_y + 1],
                } == keyword_set and {
                    grid[starting_pos_x - 1][starting_pos_y + 1],
                    grid[starting_pos_x + 1][starting_pos_y - 1],
                } == keyword_set:
                    answer += 1

    return answer


def test_run() -> None:
    expected_part_1_answer = 18
    expectd_part_2_answer = 9

    with (cwd / "example.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expectd_part_2_answer)


if __name__ == "__main__":
    with (cwd / "input.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)
    print(part_1_answer, part_2_answer)
