"""Day 22: Monkey Market.

https://adventofcode.com/2024/day/22
"""

from __future__ import annotations

from pathlib import Path


cwd = Path(__file__).parent


def run_part_1(secret_numbers: list[int]) -> int:
    sum_nth_secret_numbers = 0
    num_new_secrets = 2000

    for s_number in secret_numbers:
        for _ in range(num_new_secrets):
            s_number = ((s_number * 64) ^ s_number) % 16777216  # noqa: PLW2901
            s_number = ((s_number // 32) ^ s_number) % 16777216  # noqa: PLW2901
            s_number = ((s_number * 2048) ^ s_number) % 16777216  # noqa: PLW2901
        sum_nth_secret_numbers += s_number

    return sum_nth_secret_numbers


# TODO
def run_part_2(secret_numbers: list[int]) -> int:  # noqa: ARG001
    return -1


def run(input_data: str) -> tuple[int, int]:
    secret_numbers = list(map(int, input_data.strip().splitlines()))

    part_1_answer = run_part_1(secret_numbers)
    part_2_answer = run_part_2(secret_numbers)

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 94558292
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
