"""Day 19: Linen Layout.

https://adventofcode.com/2024/day/19
"""

from __future__ import annotations

from pathlib import Path


cwd = Path(__file__).parent


def run_part_1(towels: list[str], lines: list[str]) -> int:
    answer = 0
    for line in lines:
        letters = [False] * (len(line) + 1)
        letters[0] = True

        for i in range(1, len(line) + 1):
            for towel in towels:
                if line[i - len(towel) : i] == towel and letters[i - len(towel)]:
                    letters[i] = True
                    break
        if letters[len(line)]:
            answer += 1

    return answer


def run_part_2(towels: list[str], lines: list[str]) -> int:
    answer = 0
    for line in lines:
        letters = [0] * (len(line) + 1)
        letters[0] = 1

        for i in range(1, len(line) + 1):
            for towel in towels:
                if line[i - len(towel) : i] == towel and letters[i - len(towel)]:
                    letters[i] += letters[i - len(towel)]

        answer += letters[len(line)]
    return answer


def run(input_data: str) -> tuple[int, int]:
    unparsed_towels, unparsed_lines = input_data.split("\n\n")

    towels = [towel.strip() for towel in unparsed_towels.strip().split(",")]
    lines = unparsed_lines.strip().split("\n")

    part_1_answer = run_part_1(towels, lines)
    part_2_answer = run_part_2(towels, lines)

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 6
    expected_part_2_answer = 16

    with (cwd / "example.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expected_part_2_answer)


if __name__ == "__main__":
    with (cwd / "input.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)
    print(part_1_answer, part_2_answer)
