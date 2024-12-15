"""Day 9: Disk Fragmenter.

https://adventofcode.com/2024/day/9
"""

from __future__ import annotations

from pathlib import Path


cwd = Path(__file__).parent


def run(path_to_input_data: Path) -> tuple[int, ...]:  # noqa: C901, PLR0912
    with path_to_input_data.open("r") as file:
        input_data = file.read().replace("\n", "")

    blocks: list[int | str] = []
    file_blocks_len: list[tuple[int, int]] = []

    file_index = 0
    empty_block = "."

    for index, block_len in enumerate(input_data):
        if (index + 1) % 2 != 0 or index == 0:
            block = file_index
            file_index += 1
        else:
            block = empty_block  # type: ignore[assignment]

        exp_blocks = [block for _ in range(int(block_len))]
        if block != empty_block:  # type: ignore[comparison-overlap]
            file_blocks_len.append((block, len(exp_blocks)))

        blocks.extend(exp_blocks)

    # part 1
    part_1_sorted_blocks = blocks.copy()

    for rev_index in range(len(part_1_sorted_blocks) - 1, -1, -1):
        rev_block = part_1_sorted_blocks[rev_index]

        for index in range(len(part_1_sorted_blocks)):
            curr_block = part_1_sorted_blocks[index]
            if curr_block == empty_block:
                part_1_sorted_blocks[index] = rev_block
                break

        part_1_sorted_blocks[rev_index] = empty_block

    file_sorted_blocks: list[int] = [
        block  # type: ignore[misc]
        for block in part_1_sorted_blocks
        if block != empty_block
    ]

    part_1_answer = 0
    for index, block in enumerate(file_sorted_blocks):
        part_1_answer += block * index

    # part 2
    part_2_blocks = blocks.copy()

    file_blocks_len.sort(key=lambda x: x[0], reverse=True)

    for file_id, file_length in file_blocks_len:
        file_start = -1
        for i in range(len(part_2_blocks)):
            if part_2_blocks[i] == file_id:
                file_start = i
                break

        if file_start == -1:
            continue

        best_position = file_start
        current_position = 0

        while current_position < file_start:
            if all(
                block == empty_block
                for block in part_2_blocks[current_position : current_position + file_length]
            ):
                best_position = current_position
                break
            current_position += 1

        if best_position != file_start:
            for i in range(file_start, file_start + file_length):
                part_2_blocks[i] = empty_block
            for i in range(best_position, best_position + file_length):
                part_2_blocks[i] = file_id

    part_2_answer = 0
    for index, block in enumerate(part_2_blocks):  # type: ignore[assignment]
        if block != empty_block:  # type: ignore[comparison-overlap]
            part_2_answer += block * index

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 1928
    expectd_part_2_answer = 2858

    part_1_answer, part_2_answer = run(cwd / "example.txt")

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expectd_part_2_answer)


if __name__ == "__main__":
    part_1_answer, part_2_answer = run(cwd / "input.txt")
    print(part_1_answer, part_2_answer)
