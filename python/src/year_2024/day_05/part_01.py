"""Day 5: Print Queue (#1).

https://adventofcode.com/2024/day/5
"""

from __future__ import annotations

import pathlib
import argparse


def run(input_data: str) -> int:
    rules_section, updates_section = input_data.split("\n\n")

    rules = [tuple(map(int, unpar_rule.split("|"))) for unpar_rule in rules_section.splitlines()]
    updates = [
        list(map(int, unpar_update.split(","))) for unpar_update in updates_section.splitlines()
    ]

    correct_updates = []
    wrong_updates = []

    for update in updates:
        is_correct_order_in_update = []

        for page_index, page in enumerate(update):
            page_rules = [rule[1] for rule in rules if page == rule[0]]
            is_correct_position = [
                page_index < update.index(p_rule) for p_rule in page_rules if p_rule in update
            ]

            if not is_correct_position:
                is_correct_position = [True]

            is_correct_order = all(is_correct_position)

            is_correct_order_in_update.append(is_correct_order)

        if all(is_correct_order_in_update):
            correct_updates.append(update)

        else:
            wrong_updates.append(update)

    return sum(update[len(update) // 2] for update in correct_updates)


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 143

    with (examples_dir / "day_05.txt").open() as file:
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
