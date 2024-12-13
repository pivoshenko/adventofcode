"""Day 1: Historian Hysteria.

https://adventofcode.com/2024/day/1
"""

from __future__ import annotations

from pathlib import Path


cwd = Path(__file__).parent


def run(path_to_input_data: Path) -> tuple[int, ...]:
    with path_to_input_data.open("r") as file:
        input_data = file.read().splitlines()

    unpar_left_list, unpar_right_list = zip(*(line.split() for line in input_data), strict=False)
    left_list = sorted([int(element) for element in unpar_left_list])
    right_list = sorted([int(element) for element in unpar_right_list])

    # part 1
    distances = [
        abs(left_element - right_element)
        for left_element, right_element in zip(left_list, right_list, strict=False)
    ]
    total_distance = sum(distances)

    # part 2
    occurrences = {left_element: right_list.count(left_element) for left_element in left_list}
    similarity_score = sum(
        left_element * occurrence for left_element, occurrence in occurrences.items()
    )

    return total_distance, similarity_score


def test_run() -> None:
    expected_distances = 11
    expectd_similarity_score = 13

    distance, similarity_score = run(cwd / "example.txt")

    assert (distance, similarity_score) == (expected_distances, expectd_similarity_score)


if __name__ == "__main__":
    part_1_answer, part_2_answer = run(cwd / "input.txt")
    print(part_1_answer, part_2_answer)
