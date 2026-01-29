"""Day 9: Disk Fragmenter (#1).

https://adventofcode.com/2024/day/9
"""

from __future__ import annotations

import pathlib
import argparse


def run(input_data: str) -> int:
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

    for rev_index in range(len(sorted_blocks) - 1, -1, -1):
        rev_block = sorted_blocks[rev_index]

        for index in range(len(sorted_blocks)):
            curr_block = sorted_blocks[index]
            if curr_block == empty_block:
                sorted_blocks[index] = rev_block
                break

        sorted_blocks[rev_index] = empty_block

    file_sorted_blocks: list[int] = [block for block in sorted_blocks if block != empty_block]

    checksum = 0
    for index, block in enumerate(file_sorted_blocks):
        checksum += block * index

    return checksum


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 1928

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
