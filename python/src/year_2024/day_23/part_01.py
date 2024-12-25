"""Day 23: LAN Party (#1).

https://adventofcode.com/2024/day/23
"""

from __future__ import annotations

import pathlib
import argparse
import collections


def run(input_data: str) -> int:
    connections = [line.split("-") for line in input_data.strip().splitlines()]

    network = collections.defaultdict(list)
    for conn in connections:
        network[conn[0]].append(conn[1])
        network[conn[1]].append(conn[0])

    inter_connections: set[tuple[str, ...]] = set()
    for node_1 in network:
        if node_1[0] == "t":
            neighbours_1 = network[node_1]
            for node_2 in neighbours_1:
                neighbours_2 = network[node_2]
                for node_3 in neighbours_2:
                    if node_3 in neighbours_1:
                        nodes = tuple(sorted((node_1, node_2, node_3)))
                        inter_connections.add(nodes)

    return len(inter_connections)


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = 7

    with (examples_dir / "day_23.txt").open() as file:
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
