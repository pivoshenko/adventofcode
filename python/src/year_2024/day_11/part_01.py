"""Day 11: Plutonian Pebbles (#1).

https://adventofcode.com/2024/day/11
"""

from __future__ import annotations

import pathlib
import argparse
import functools


def blink_dfs(blinks: int, stones: list[str]) -> int:
    @functools.cache
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


def run(input_data: str) -> int:
    initial_stones = [char.replace("\n", "") for char in input_data.split(" ")]

    return blink_dfs(25, initial_stones)


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 55312

    with (examples_dir / "day_11.txt").open() as file:
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
