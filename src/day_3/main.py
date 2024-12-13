"""Day 3: Mull It Over.

https://adventofcode.com/2024/day/3
"""

from __future__ import annotations

import re

from pathlib import Path


cwd = Path(__file__).parent


def run(path_to_input_data: Path) -> tuple[int, int]:
    with path_to_input_data.open("r") as file:
        input_data = file.read()

    # part 1
    instruction_pattern = r"mul\(\d+,\s*\d+\)"
    instructions = re.findall(instruction_pattern, input_data)

    numbers_pattern = r"\d+"
    part_1_answer = 0
    for instruction in instructions:
        left, right = re.findall(numbers_pattern, instruction)
        part_1_answer += int(left) * int(right)

    print(part_1_answer)

    # part 2
    new_instruction_pattern = r"mul\(\d+,\s*\d+\)|don't|do"
    new_instructions = re.findall(new_instruction_pattern, input_data)

    part_2_answer = 0
    is_do = True
    for instruction in new_instructions:
        if instruction == "don't":
            is_do = False
            continue

        if instruction == "do":
            is_do = True
            continue

        if is_do:
            left, right = re.findall(numbers_pattern, instruction)
            part_2_answer += int(left) * int(right)

    print(part_2_answer)

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 161
    expectd_part_2_answer = 48

    part_1_answer, part_2_answer = run(cwd / "example.txt")
    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expectd_part_2_answer)


if __name__ == "__main__":
    run(cwd / "input.txt")
