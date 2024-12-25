"""Day 17: Chronospatial Computer (#1).

https://adventofcode.com/2024/day/17
"""

from __future__ import annotations

import re
import pathlib
import argparse


def run(input_data: str) -> str:  # noqa: C901
    unparsed_registers, unparsed_program = input_data.strip().split("\n\n")
    registers = list(map(int, re.findall(r"-?\d+", unparsed_registers)))
    program = list(map(int, re.findall(r"-?\d+", unparsed_program)))

    a, b, c = registers
    instruction_pointer = 0
    output = []

    while instruction_pointer < len(program):
        opcode = program[instruction_pointer]
        operand = program[instruction_pointer + 1] if instruction_pointer + 1 < len(program) else 0

        def combo_value(op: int) -> int:
            if op <= 3:
                return op
            if op == 4:
                return a
            if op == 5:
                return b
            if op == 6:
                return c
            return 0

        if opcode == 0:  # adv
            a //= 2 ** combo_value(operand)
        elif opcode == 1:  # bxl
            b ^= operand
        elif opcode == 2:  # bst
            b = combo_value(operand) % 8
        elif opcode == 3:  # jnz
            if a != 0:
                instruction_pointer = operand
                continue
        elif opcode == 4:  # bxc
            b ^= c
        elif opcode == 5:  # out
            output.append(combo_value(operand) % 8)
        elif opcode == 6:  # bdv
            b = a // (2 ** combo_value(operand))
        elif opcode == 7:  # cdv
            c = a // (2 ** combo_value(operand))

        instruction_pointer += 2

    return ",".join(map(str, output))


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = "4,6,3,5,6,3,5,2,1,0"

    with (examples_dir / "day_17.txt").open() as file:
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
