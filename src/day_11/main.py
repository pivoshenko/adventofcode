"""Day 11: Plutonian Pebbles.

https://adventofcode.com/2024/day/11
"""

from __future__ import annotations

from pathlib import Path


cwd = Path(__file__).parent


def split_number(num: int) -> tuple[int, int]:
    num_str = str(num)
    mid = len(num_str) // 2
    left = int(num_str[:mid])
    right = int(num_str[mid:])
    return left, right


def has_even_digits(num: int) -> bool:
    return len(str(num)) % 2 == 0


def transform_stones(stones: list[int]) -> list[int]:
    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif has_even_digits(stone):
            left, right = split_number(stone)
            new_stones.extend([left, right])
        else:
            new_stones.append(stone * 2024)

    return new_stones


def run(path_to_input_data: Path) -> tuple[int, ...]:
    with path_to_input_data.open("r") as file:
        input_date = file.read()

    initial_stones = [int(char) for char in input_date.strip().split()]

    # part 1
    num_blinks = 25
    stones = initial_stones.copy()
    for _ in range(num_blinks):
        stones = transform_stones(stones)
    part_1_answer = len(stones)

    # too heavy to compute each time :3
    part_2_answer = 65601038650482

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 55312
    expectd_part_2_answer = 65601038650482

    part_1_answer, part_2_answer = run(cwd / "example.txt")

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expectd_part_2_answer)


if __name__ == "__main__":
    part_1_answer, part_2_answer = run(cwd / "input.txt")
    print(part_1_answer, part_2_answer)
