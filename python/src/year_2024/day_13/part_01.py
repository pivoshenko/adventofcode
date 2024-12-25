"""Day 13: Claw Contraption (#1).

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
    max_tokens = 100

    for machine_params in machines_params:
        a_x, a_y, b_x, b_y, p_x, p_y = machine_params
        min_cost = float("inf")
        is_solved = False

        for a_press in range(max_tokens):
            for b_press in range(max_tokens):
                c_x = a_x * a_press + b_x * b_press
                c_y = a_y * a_press + b_y * b_press
                if c_x == p_x and c_y == p_y:
                    curr_cost = a_press * a_press_cost + b_press * b_press_cost
                    if curr_cost < min_cost:
                        min_cost = curr_cost
                        is_solved = True

        if is_solved:
            total_cost += min_cost  # type: ignore[assignment]

    return total_cost


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 480

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
