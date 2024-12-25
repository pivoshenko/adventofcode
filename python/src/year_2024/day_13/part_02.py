"""Day 13: Claw Contraption (#2).

https://adventofcode.com/2024/day/13
"""

from __future__ import annotations

import re
import pathlib
import argparse


def parse_machine_params(machine: str) -> list[int]:
    params = []
    for line in machine.splitlines():
        numbers = re.findall(r"\d+", line)
        params.extend(list(map(int, numbers)))
    return params


def run(input_data: str) -> int:
    machines_def = input_data.strip().split("\n\n")
    machines_params = list(map(parse_machine_params, machines_def))

    a_press_cost = 3
    b_press_cost = 1

    total_cost = 0
    offset = 10000000000000
    for machine_params in machines_params:
        a_x, a_y, b_x, b_y, p_x, p_y = machine_params
        p_x += offset
        p_y += offset

        # Cramer's rule
        x = (p_x * b_y - b_x * p_y) / (a_x * b_y - b_x * a_y)
        y = (a_x * p_y - p_x * a_y) / (a_x * b_y - b_x * a_y)

        if x.is_integer() and y.is_integer():
            total_cost += int(x * a_press_cost + y * b_press_cost)

    return total_cost


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 875318608908

    with (examples_dir / "day_13.txt").open() as file:
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
