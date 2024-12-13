"""Day 6: Guard Gallivant.

https://adventofcode.com/2024/day/6

# !!! BRUTEFOCE !!!
# I am doing it when I have super limited time :3
TODO REFACTOR IT!
"""

from __future__ import annotations

from pathlib import Path


cwd = Path(__file__).parent


def print_grid(grid: list[list[str]]) -> None:
    print("\n".join(["".join(line) for line in grid]), end="\n\n\n")


def count_visited_tiles(
    grid: list[list[str]],
    tile: str,
    obstacle: str,
) -> int:
    rows = len(grid)
    cols = len(grid[0])
    counter = 0
    for y in range(rows):
        for x in range(cols):
            if grid[y][x] not in (tile, obstacle):
                counter += 1
    return counter


def run(path_to_input_data: Path) -> int:  # noqa: C901, PLR0912, PLR0915
    with path_to_input_data.open("r") as file:
        input_data = file.read()

    grid = [list(line) for line in input_data.splitlines()]
    rows = len(grid)
    cols = len(grid[0])

    tile = "."
    obstacle = "#"
    visited = "X"

    guard_up = "^"
    guard_up_dir = (0, 1)  # <x, y>

    guard_down = "v"
    guard_down_dir = (0, -1)  # <x, y>

    guard_right = ">"
    guard_right_dir = (1, 0)  # <x, y>

    guard_left = "<"
    guard_left_dir = (-1, 0)  # <x, y>

    curr_guard_pos_y = -1
    curr_guard_pos_x = -1
    curr_guard_dir = ""

    for y in range(rows):
        for x in range(cols):
            if grid[y][x] not in (tile, obstacle):
                curr_guard_pos_x = x
                curr_guard_pos_y = y
                curr_guard_dir = grid[y][x]

    print_grid(grid)

    try:
        while True:
            if curr_guard_dir == guard_up:
                new_guard_pos_x = curr_guard_pos_x + guard_up_dir[0]
                new_guard_pos_y = curr_guard_pos_y - guard_up_dir[1]

                if grid[new_guard_pos_y][new_guard_pos_x] != obstacle:
                    grid[new_guard_pos_y][new_guard_pos_x] = guard_up
                    grid[curr_guard_pos_y][curr_guard_pos_x] = visited
                    curr_guard_pos_x = new_guard_pos_x
                    curr_guard_pos_y = new_guard_pos_y
                    curr_guard_dir = guard_up
                    print_grid(grid)

                else:
                    new_guard_pos_x = curr_guard_pos_x + guard_right_dir[0]
                    new_guard_pos_y = curr_guard_pos_y + guard_right_dir[1]
                    if grid[new_guard_pos_y][new_guard_pos_x] != obstacle:
                        grid[new_guard_pos_y][new_guard_pos_x] = guard_right
                        grid[curr_guard_pos_y][curr_guard_pos_x] = visited
                        curr_guard_pos_x = new_guard_pos_x
                        curr_guard_pos_y = new_guard_pos_y
                        curr_guard_dir = guard_right
                        print_grid(grid)

            if curr_guard_dir == guard_right:
                new_guard_pos_x = curr_guard_pos_x + guard_right_dir[0]
                new_guard_pos_y = curr_guard_pos_y + guard_right_dir[1]
                if grid[new_guard_pos_y][new_guard_pos_x] != obstacle:
                    grid[new_guard_pos_y][new_guard_pos_x] = guard_right
                    grid[curr_guard_pos_y][curr_guard_pos_x] = visited
                    curr_guard_pos_x = new_guard_pos_x
                    curr_guard_pos_y = new_guard_pos_y
                    curr_guard_dir = guard_right
                    print_grid(grid)

                else:
                    new_guard_pos_x = curr_guard_pos_x + guard_down_dir[0]
                    new_guard_pos_y = curr_guard_pos_y - guard_down_dir[1]
                    if grid[new_guard_pos_y][new_guard_pos_x] != obstacle:
                        grid[new_guard_pos_y][new_guard_pos_x] = guard_down
                        grid[curr_guard_pos_y][curr_guard_pos_x] = visited
                        curr_guard_pos_x = new_guard_pos_x
                        curr_guard_pos_y = new_guard_pos_y
                        curr_guard_dir = guard_down
                        print_grid(grid)

            if curr_guard_dir == guard_down:
                new_guard_pos_x = curr_guard_pos_x + guard_down_dir[0]
                new_guard_pos_y = curr_guard_pos_y - guard_down_dir[1]
                if grid[new_guard_pos_y][new_guard_pos_x] != obstacle:
                    grid[new_guard_pos_y][new_guard_pos_x] = guard_down
                    grid[curr_guard_pos_y][curr_guard_pos_x] = visited
                    curr_guard_pos_x = new_guard_pos_x
                    curr_guard_pos_y = new_guard_pos_y
                    curr_guard_dir = guard_down
                    print_grid(grid)

                else:
                    new_guard_pos_x = curr_guard_pos_x + guard_left_dir[0]
                    new_guard_pos_y = curr_guard_pos_y + guard_left_dir[1]
                    if grid[new_guard_pos_y][new_guard_pos_x] != obstacle:
                        grid[new_guard_pos_y][new_guard_pos_x] = guard_left
                        grid[curr_guard_pos_y][curr_guard_pos_x] = visited
                        curr_guard_pos_x = new_guard_pos_x
                        curr_guard_pos_y = new_guard_pos_y
                        curr_guard_dir = guard_left
                        print_grid(grid)

            if curr_guard_dir == guard_left:
                new_guard_pos_x = curr_guard_pos_x + guard_left_dir[0]
                new_guard_pos_y = curr_guard_pos_y + guard_left_dir[1]
                if grid[new_guard_pos_y][new_guard_pos_x] != obstacle:
                    grid[new_guard_pos_y][new_guard_pos_x] = guard_left
                    grid[curr_guard_pos_y][curr_guard_pos_x] = visited
                    curr_guard_pos_x = new_guard_pos_x
                    curr_guard_pos_y = new_guard_pos_y
                    curr_guard_dir = guard_left
                    print_grid(grid)

                else:
                    new_guard_pos_x = curr_guard_pos_x + guard_up_dir[0]
                    new_guard_pos_y = curr_guard_pos_y - guard_up_dir[1]

                    if grid[new_guard_pos_y][new_guard_pos_x] != obstacle:
                        grid[new_guard_pos_y][new_guard_pos_x] = guard_up
                        grid[curr_guard_pos_y][curr_guard_pos_x] = visited
                        curr_guard_pos_x = new_guard_pos_x
                        curr_guard_pos_y = new_guard_pos_y
                        curr_guard_dir = guard_up
                        print_grid(grid)
    except IndexError:
        answer = count_visited_tiles(grid, tile=tile, obstacle=obstacle)

    return answer


def test_run() -> None:
    expected_part_1_answer = 41

    part_1_answer = run(cwd / "example.txt")

    assert part_1_answer == expected_part_1_answer


if __name__ == "__main__":
    part_1_answer = run(cwd / "input.txt")
    print(part_1_answer)
