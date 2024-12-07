"""Day 1: Historian Hysteria.

https://adventofcode.com/2024/day/1
"""

from __future__ import annotations

from pathlib import Path


def run() -> None:  # noqa: D103
    path_to_input_data = Path(__file__).parent / "input.txt"

    with path_to_input_data.open("r") as file:
        input_data = file.read().splitlines()

    left_list, right_list = zip(*(line.split() for line in input_data), strict=False)
    left_list = sorted([int(element) for element in left_list])  # type: ignore[assignment]
    right_list = sorted([int(element) for element in right_list])  # type: ignore[assignment]

    # part 1
    distances = [
        abs(left_element - right_element)
        for left_element, right_element in zip(left_list, right_list, strict=False)
    ]
    total_distance = sum(distances)
    print(total_distance)

    # part 2
    occurrences = {left_element: right_list.count(left_element) for left_element in left_list}
    similarity_score = sum(
        left_element * occurrence for left_element, occurrence in occurrences.items()
    )
    print(similarity_score)


if __name__ == "__main__":
    run()
