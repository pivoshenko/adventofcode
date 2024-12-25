"""Day 24: Crossed Wires.

https://adventofcode.com/2024/day/24
"""

from __future__ import annotations

import re
import collections

from pathlib import Path


cwd = Path(__file__).parent


def run_part_1(gates: dict[str, int], operations: list[list[str]]) -> int:
    while True:
        gates_values = list(gates.values())[:]

        for gate_1, operator, gate_2, gate_3 in operations:
            if operator == "AND":
                gates[gate_3] = int(gates[gate_1] and gates[gate_2])
            elif operator == "XOR":
                gates[gate_3] = int(gates[gate_1] != gates[gate_2])
            else:
                gates[gate_3] = int(gates[gate_1] or gates[gate_2])

        if gates_values == list(gates.values()):
            break

    gates_sort = sorted(gates.keys(), reverse=True)
    bin_n = ""
    for gate in gates_sort:
        if gate[0] == "z":
            bin_n += str(gates[gate])

    return int(bin_n, 2)


# TODO
def run_part_2() -> int:
    return -1


def run(input_data: str) -> tuple[int, int]:
    unparsed_gates, unparsed_operations = input_data.split("\n\n")

    gates = collections.defaultdict(int)
    for line in unparsed_gates.splitlines():
        gate, value = list(re.findall(r"([a-zA-Z]+\d+): (\d)", line.strip())[0])
        gates[gate] = int(value)

    pattern = r"([a-zA-Z0-9]+)\s+(AND|XOR|OR)\s+([a-zA-Z0-9]+)\s+->\s+([a-zA-Z0-9]+)"
    operations = [
        list(re.findall(pattern, line.strip())[0]) for line in unparsed_operations.splitlines()
    ]

    part_1_answer = run_part_1(gates, operations)
    part_2_answer = run_part_2()

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 2024
    expected_part_2_answer = -1

    with (cwd / "example.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expected_part_2_answer)


if __name__ == "__main__":
    with (cwd / "input.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)
    print(part_1_answer, part_2_answer)
