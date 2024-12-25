"""Day 2: Red-Nosed Reports (#1).

https://adventofcode.com/2024/day/2
"""

from __future__ import annotations

import pathlib
import argparse
import itertools


def check(report: list[int]) -> bool:
    diffs = [el_1 - el_2 for el_1, el_2 in itertools.pairwise(report)]
    max_diff = max(abs(diff) for diff in diffs)

    is_trend_increasing = all(el_1 < el_2 for el_1, el_2 in itertools.pairwise(report))
    is_trend_decreasing = all(el_1 > el_2 for el_1, el_2 in itertools.pairwise(report))

    return max_diff <= 3 and (is_trend_increasing or is_trend_decreasing)


def run(input_data: str) -> int:
    reports = [list(map(int, line.split())) for line in input_data.splitlines()]
    return len(list(filter(check, reports)))


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 2

    with (examples_dir / "day_02.txt").open() as file:
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
