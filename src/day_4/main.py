"""Day 4: Ceres Search.

https://adventofcode.com/2024/day/4
"""

from __future__ import annotations

from pathlib import Path


def run_part_1() -> None:
    path_to_input_data = Path(__file__).parent / "input.txt"

    with path_to_input_data.open("r") as file:
        input_data = file.read()

    keyword = "XMAS"

    grid = input_data.splitlines()
    rows = len(grid)
    cols = len(grid[0])
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

    print(answer)


def run_part_2() -> None:
    path_to_input_data = Path(__file__).parent / "input.txt"

    with path_to_input_data.open("r") as file:
        input_data = file.read()

    grid = input_data.splitlines()
    rows = len(grid)
    cols = len(grid[0])
    _set = {"M", "S"}

    answer = 0

    for starting_pos_x in range(1, rows - 1):
        for starting_pos_y in range(1, cols - 1):
            if grid[starting_pos_x][starting_pos_y] == "A":  # noqa: SIM102
                if {
                    grid[starting_pos_x - 1][starting_pos_y - 1],
                    grid[starting_pos_x + 1][starting_pos_y + 1],
                } == _set and {
                    grid[starting_pos_x - 1][starting_pos_y + 1],
                    grid[starting_pos_x + 1][starting_pos_y - 1],
                } == _set:
                    answer += 1

    print(answer)


if __name__ == "__main__":
    run_part_1()
    run_part_2()