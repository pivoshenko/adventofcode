"""Day 1: Historian Hysteria (#2).

https://adventofcode.com/2024/day/1
"""

from __future__ import annotations

import pathlib
import argparse


def run(input_data: str) -> int:
    left_part, right_part = zip(
        *(line.split() for line in input_data.splitlines()),
        strict=False,
    )
    left_list = sorted(map(int, left_part))
    right_list = sorted(map(int, right_part))

    occurrences = {left_element: right_list.count(left_element) for left_element in left_list}
    return sum(left_element * occurrence for left_element, occurrence in occurrences.items())


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 13

    with (examples_dir / "day_01.txt").open() as file:
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
