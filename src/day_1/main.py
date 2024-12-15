"""Day 1: Historian Hysteria.

https://adventofcode.com/2024/day/1
"""

from __future__ import annotations

from pathlib import Path


cwd = Path(__file__).parent


def run(input_data: str) -> tuple[int, int]:
    unpar_left_list, unpar_right_list = zip(
        *(line.split() for line in input_data.splitlines()),
        strict=False,
    )
    left_list = sorted(map(int, unpar_left_list))
    right_list = sorted(map(int, unpar_right_list))

    # part 1
    distances = [
        abs(left_element - right_element)
        for left_element, right_element in zip(left_list, right_list, strict=False)
    ]
    part_1_answer = sum(distances)

    # part 2
    occurrences = {left_element: right_list.count(left_element) for left_element in left_list}
    part_2_answer = sum(
        left_element * occurrence for left_element, occurrence in occurrences.items()
    )

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 11
    expectd_part_2_answer = 13

    with (cwd / "example.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expectd_part_2_answer)


if __name__ == "__main__":
    with (cwd / "input.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)
    print(part_1_answer, part_2_answer)
