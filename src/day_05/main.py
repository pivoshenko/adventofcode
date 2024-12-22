"""Day 5: Print Queue.

https://adventofcode.com/2024/day/5
"""

from __future__ import annotations

from pathlib import Path


cwd = Path(__file__).parent


def run(input_data: str) -> tuple[int, int]:
    unpar_rules, unpar_updates = input_data.split("\n\n")

    rules = [tuple(map(int, unpar_rule.split("|"))) for unpar_rule in unpar_rules.splitlines()]
    updates = [
        list(map(int, unpar_update.split(","))) for unpar_update in unpar_updates.splitlines()
    ]

    # part 1
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

    part_1_answer = sum(update[len(update) // 2] for update in correct_updates)

    # part 2
    corrected_updates = []
    for update in wrong_updates:
        corrected_update = update.copy()

        for _ in range(len(corrected_update)):
            for page, page_rule in rules:
                if page in corrected_update and page_rule in corrected_update:
                    page_index = corrected_update.index(page)
                    page_rule_index = corrected_update.index(page_rule)
                    if page_index > page_rule_index:
                        corrected_update[page_index], corrected_update[page_rule_index] = (
                            corrected_update[page_rule_index],
                            corrected_update[page_index],
                        )

        corrected_updates.append(corrected_update)

    part_2_answer = sum(update[len(update) // 2] for update in corrected_updates)

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 143
    expectd_part_2_answer = 123

    with (cwd / "example.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expectd_part_2_answer)


if __name__ == "__main__":
    with (cwd / "input.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)
    print(part_1_answer, part_2_answer)