"""Day 3: Mull It Over (#2).

https://adventofcode.com/2024/day/3
"""

from __future__ import annotations

import re
import pathlib
import argparse


def run(input_data: str) -> int:
    new_instruction_pattern = r"mul\(\d+,\s*\d+\)|don't|do"
    new_instructions = re.findall(new_instruction_pattern, input_data)

    numbers_pattern = r"\d+"

    is_do = True
    enabled_multiplications = 0
    for instruction in new_instructions:
        if instruction == "don't":
            is_do = False
            continue

        if instruction == "do":
            is_do = True
            continue

        if is_do:
            left, right = re.findall(numbers_pattern, instruction)
            enabled_multiplications += int(left) * int(right)

    return enabled_multiplications


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 48

    with (examples_dir / "day_03.txt").open() as file:
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
