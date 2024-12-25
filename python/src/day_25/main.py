"""Day 25: Code Chronicle.

https://adventofcode.com/2024/day/25
"""

from __future__ import annotations

from pathlib import Path


cwd = Path(__file__).parent


def run_part_1(transmit_bloks: list[list[str]]) -> int:
    pin_heights = [
        [sum([2**i for i in range(len(block)) if block[i][j] == "#"]) for j in range(5)]
        for block in transmit_bloks
    ]
    ctr = 0
    for i in range(len(pin_heights)):
        for j in range(i + 1, len(pin_heights)):
            if all(pin_heights[i][k] & pin_heights[j][k] == 0 for k in range(5)):
                ctr += 1
    return ctr


# TODO
def run_part_2() -> int:
    return -1


def run(input_data: str) -> tuple[int, str]:
    lines = input_data.splitlines()
    transmit_bloks = [lines[i : i + 7] for i in range(0, len(lines), 8)]

    part_1_answer = run_part_1(transmit_bloks)
    part_2_answer = run_part_2()

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 3
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
