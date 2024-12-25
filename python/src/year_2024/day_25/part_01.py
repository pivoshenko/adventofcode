"""Day 25: Code Chronicle (#1).

https://adventofcode.com/2024/day/25
"""

from __future__ import annotations

import pathlib
import argparse


def run(input_data: str) -> int:
    lines = input_data.splitlines()
    transmit_bloks = [lines[i : i + 7] for i in range(0, len(lines), 8)]

    pin_heights = [
        [sum([2**i for i in range(len(block)) if block[i][j] == "#"]) for j in range(5)]
        for block in transmit_bloks
    ]
    ctr = 0
    for i in range(len(pin_heights)):
        for j in range(i + 1, len(pin_heights)):
            if all(pin_heights[i][k] & pin_heights[j][k] == 0 for k in range(5)):
                ctr += 1
    return ctr


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 3

    with (examples_dir / "day_25.txt").open() as file:
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
