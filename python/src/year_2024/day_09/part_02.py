"""Day 9: Disk Fragmenter (#2).

https://adventofcode.com/2024/day/9
"""

from __future__ import annotations

import pathlib
import argparse


def run(input_data: str) -> int:  # noqa: C901, PLR0912
    blocks: list[int] = []
    file_blocks_len: list[tuple[int, int]] = []

    file_index = 0
    empty_block = -1

    for index, block_len in enumerate(input_data.replace("\n", "")):
        if (index + 1) % 2 != 0 or index == 0:
            block = file_index
            file_index += 1
        else:
            block = empty_block

        exp_blocks = [block for _ in range(int(block_len))]
        if block != empty_block:
            file_blocks_len.append((block, len(exp_blocks)))

        blocks.extend(exp_blocks)

    sorted_blocks = blocks.copy()

    file_blocks_len.sort(key=lambda x: x[0], reverse=True)

    for file_id, file_length in file_blocks_len:
        file_start = -1
        for i in range(len(sorted_blocks)):
            if sorted_blocks[i] == file_id:
                file_start = i
                break

        if file_start == -1:
            continue

        best_position = file_start
        current_position = 0

        while current_position < file_start:
            if all(
                block == empty_block
                for block in sorted_blocks[current_position : current_position + file_length]
            ):
                best_position = current_position
                break
            current_position += 1

        if best_position != file_start:
            for i in range(file_start, file_start + file_length):
                sorted_blocks[i] = empty_block
            for i in range(best_position, best_position + file_length):
                sorted_blocks[i] = file_id

    checksum = 0
    for index, block in enumerate(sorted_blocks):
        if block != empty_block:
            checksum += block * index

    return checksum


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 2858

    with (examples_dir / "day_09.txt").open() as file:
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
