"""Day 22: Monkey Market (#1).

https://adventofcode.com/2024/day/22
"""

from __future__ import annotations

import pathlib
import argparse


def run(input_data: str) -> int:
    secret_numbers = list(map(int, input_data.strip().splitlines()))

    sum_nth_secret_numbers = 0
    num_new_secrets = 2000

    for s_number in secret_numbers:
        for _ in range(num_new_secrets):
            s_number = ((s_number * 64) ^ s_number) % 16777216  # noqa: PLW2901
            s_number = ((s_number // 32) ^ s_number) % 16777216  # noqa: PLW2901
            s_number = ((s_number * 2048) ^ s_number) % 16777216  # noqa: PLW2901
        sum_nth_secret_numbers += s_number

    return sum_nth_secret_numbers


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 94558292

    with (examples_dir / "day_22.txt").open() as file:
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
