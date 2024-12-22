"""Day 17: Chronospatial Computer.

https://adventofcode.com/2024/day/17
"""

from __future__ import annotations

from pathlib import Path
import re


cwd = Path(__file__).parent


def run_part_1(registers: list[int], program: list[int]) -> str:  # noqa: C901
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


def run(input_data: str) -> tuple[str, int]:
    unparsed_registers, unparsed_program = input_data.strip().split("\n\n")
    registers = list(map(int, re.findall(r"-?\d+", unparsed_registers)))
    program = list(map(int, re.findall(r"-?\d+", unparsed_program)))

    print(input_data)
    print(registers)
    print(program)

    part_1_answer = run_part_1(registers, program)
    part_2_answer = 0

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = "4,6,3,5,6,3,5,2,1,0"
    expected_part_2_answer = 0

    with (cwd / "example.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expected_part_2_answer)


if __name__ == "__main__":
    with (cwd / "example.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)
    print(part_1_answer, part_2_answer)
