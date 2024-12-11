"""Day 2: Red-Nosed Reports.

https://adventofcode.com/2024/day/2
"""

from __future__ import annotations

import itertools

from pathlib import Path


cwd = Path(__file__).parent


def check(report: list[int]) -> bool:
    diffs = [el_1 - el_2 for el_1, el_2 in itertools.pairwise(report)]
    max_diff = max(abs(diff) for diff in diffs)

    is_trend_increasing = all(el_1 < el_2 for el_1, el_2 in itertools.pairwise(report))
    is_trend_decreasing = all(el_1 > el_2 for el_1, el_2 in itertools.pairwise(report))

    return max_diff <= 3 and (is_trend_increasing or is_trend_decreasing)  # noqa: PLR2004


def run(path_to_input_data: Path) -> tuple[int, int]:
    with path_to_input_data.open("r") as file:
        input_data = file.read().splitlines()

    reports = [[int(el) for el in line.split()] for line in input_data]

    # part 1
    safe_reports = []
    unsafe_reports = []

    for report in reports:
        if check(report):
            safe_reports.append(report)

        else:
            unsafe_reports.append(report)

    part_1_answer = len(safe_reports)
    print(part_1_answer)

    # part 2
    updated_safe_reports = []

    for report in unsafe_reports:
        for index in range(len(report)):
            mod_report = report[:index] + report[index + 1 :]
            if check(mod_report):
                updated_safe_reports.append(report)
                break

    part_2_answer = len(safe_reports) + len(updated_safe_reports)
    print(len(safe_reports) + len(updated_safe_reports))

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 2
    expectd_part_2_answer = 4

    part_1_answer, part_2_answer = run(cwd / "example.txt")
    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expectd_part_2_answer)


if __name__ == "__main__":
    run(cwd / "input.txt")
