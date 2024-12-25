"""Day 19: Linen Layout (#1).

https://adventofcode.com/2024/day/19
"""

from __future__ import annotations

import pathlib
import argparse


def run(input_data: str) -> int:
    unparsed_towels, unparsed_lines = input_data.split("\n\n")

    towels = [towel.strip() for towel in unparsed_towels.strip().split(",")]
    lines = unparsed_lines.strip().split("\n")

    num_designs = 0
    for line in lines:
        letters = [False] * (len(line) + 1)
        letters[0] = True

        for i in range(1, len(line) + 1):
            for towel in towels:
                if line[i - len(towel) : i] == towel and letters[i - len(towel)]:
                    letters[i] = True
                    break
        if letters[len(line)]:
            num_designs += 1

    return num_designs


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 6

    with (examples_dir / "day_19.txt").open() as file:
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
