"""Day 13: Claw Contraption.

https://adventofcode.com/2024/day/13
"""

from __future__ import annotations

import re

from pathlib import Path


cwd = Path(__file__).parent


def parse_machine_params(machine: str) -> list[int]:
    params = []
    for line in machine.splitlines():
        numbers = re.findall(r"\d+", line)
        params.extend(list(map(int, numbers)))
    return params


def run_part_1(machines_params: list[list[int]], a_press_cost: int, b_press_cost: int) -> int:
    answer = 0
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
            answer += min_cost  # type: ignore[assignment]

    return answer


def run_part_2(machines_params: list[list[int]], a_press_cost: int, b_press_cost: int) -> int:
    answer = 0
    offset = 10000000000000
    for machine_params in machines_params:
        a_x, a_y, b_x, b_y, p_x, p_y = machine_params
        p_x += offset
        p_y += offset

        # Cramer's rule
        x = (p_x * b_y - b_x * p_y) / (a_x * b_y - b_x * a_y)
        y = (a_x * p_y - p_x * a_y) / (a_x * b_y - b_x * a_y)

        if x.is_integer() and y.is_integer():
            answer += int(x * a_press_cost + y * b_press_cost)

    return answer


def run(input_data: str) -> tuple[int, int]:
    machines_def = input_data.strip().split("\n\n")
    machines_params = list(map(parse_machine_params, machines_def))

    a_press_cost = 3
    b_press_cost = 1

    part_1_answer = run_part_1(machines_params, a_press_cost, b_press_cost)
    part_2_answer = run_part_2(machines_params, a_press_cost, b_press_cost)

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 480
    expected_part_2_answer = 875318608908

    with (cwd / "example.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expected_part_2_answer)


if __name__ == "__main__":
    with (cwd / "input.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)
    print(part_1_answer, part_2_answer)
