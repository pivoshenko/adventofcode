"""Day 7: Bridge Repair.

https://adventofcode.com/2024/day/7
"""

from __future__ import annotations

import itertools

from pathlib import Path


cwd = Path(__file__).parent


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


def run(path_to_input_data: Path) -> tuple[int, ...]:
    with path_to_input_data.open("r") as file:
        input_data = file.read()

    equations = list(map(parse_equation, input_data.splitlines()))

    # part 1
    part_1_answer = 0
    nonvalid_equations = []
    for result, numbers in equations:
        if is_equation_valid(result, numbers, "+*"):
            part_1_answer += result
        else:
            nonvalid_equations.append((result, numbers))

    # part 2
    part_2_answer = 0
    for result, numbers in nonvalid_equations:
        if is_equation_valid(result, numbers, "+*|"):
            part_2_answer += result

    part_2_answer = part_1_answer + part_2_answer

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 3749
    expectd_part_2_answer = 11387

    part_1_answer, part_2_answer = run(cwd / "example.txt")

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expectd_part_2_answer)


if __name__ == "__main__":
    part_1_answer, part_2_answer = run(cwd / "input.txt")
    print(part_1_answer, part_2_answer)
