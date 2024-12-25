"""Day 7: Bridge Repair (#1).

https://adventofcode.com/2024/day/7
"""

from __future__ import annotations

import pathlib
import argparse
import itertools


def parse_equation(unpar_equation: str) -> tuple[int, list[int]]:
    result, numbers = unpar_equation.split(": ")
    return int(result), [int(num) for num in numbers.split()]


def evaluate_left_to_right(operands: list[int], operators: tuple[str, ...]) -> int:
    result = operands[0]
    for index, operator in enumerate(operators):
        if operator == "+":
            result += operands[index + 1]
        elif operator == "*":
            result *= operands[index + 1]
        elif operator == "|":
            result = int(f"{result}{operands[index + 1]}")
    return result


def is_equation_valid(result: int, numbers: list[int], operators: str) -> bool:
    num_positions = len(numbers) - 1
    for ops in itertools.product(operators, repeat=num_positions):
        if evaluate_left_to_right(numbers, ops) == result:
            return True
    return False


def run(input_data: str) -> int:
    equations = list(map(parse_equation, input_data.splitlines()))

    total_calibration = 0
    for result, numbers in equations:
        if is_equation_valid(result, numbers, "+*"):
            total_calibration += result

    return total_calibration


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 3749

    with (examples_dir / "day_07.txt").open() as file:
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
