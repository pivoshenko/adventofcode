"""Day 11: Plutonian Pebbles.

https://adventofcode.com/2024/day/11
"""

from __future__ import annotations

from functools import cache
from pathlib import Path


cwd = Path(__file__).parent


def blink_dfs(blinks: int, stones: list[str]) -> int:
    @cache
    def dfs_helper(val: str, to_go: int) -> int:
        if to_go == 0:
            return 1
        if val == "0":
            return dfs_helper("1", to_go - 1)
        if len(val) % 2 == 0:
            n = len(val) // 2
            left = val[:n]
            right = val[n:]
            while right.startswith("0") and len(right) > 1:
                right = right[1:]
            return dfs_helper(left, to_go - 1) + dfs_helper(right, to_go - 1)
        return dfs_helper(str(int(val) * 2024), to_go - 1)

    return sum([dfs_helper(val, blinks) for val in stones])


def run(input_data: str) -> tuple[int, int]:
    initial_stones = [char.replace("\n", "") for char in input_data.split(" ")]

    part_1_answer = blink_dfs(25, initial_stones)
    part_2_answer = blink_dfs(75, initial_stones)

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 55312
    expectd_part_2_answer = 65601038650482

    with (cwd / "example.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expectd_part_2_answer)


if __name__ == "__main__":
    with (cwd / "input.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)
    print(part_1_answer, part_2_answer)
