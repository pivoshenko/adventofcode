"""Day 24: Crossed Wires (#1).

https://adventofcode.com/2024/day/24
"""

from __future__ import annotations

import re
import pathlib
import argparse
import collections


def run(input_data: str) -> int:
    unparsed_gates, unparsed_operations = input_data.split("\n\n")

    gates = collections.defaultdict(int)
    for line in unparsed_gates.splitlines():
        gate, value = list(re.findall(r"([a-zA-Z]+\d+): (\d)", line.strip())[0])
        gates[gate] = int(value)

    pattern = r"([a-zA-Z0-9]+)\s+(AND|XOR|OR)\s+([a-zA-Z0-9]+)\s+->\s+([a-zA-Z0-9]+)"
    operations = [
        list(re.findall(pattern, line.strip())[0]) for line in unparsed_operations.splitlines()
    ]

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


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 2024

    with (examples_dir / "day_24.txt").open() as file:
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
