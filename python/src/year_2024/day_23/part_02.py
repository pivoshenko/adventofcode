"""Day 23: LAN Party (#2).

https://adventofcode.com/2024/day/23
"""

from __future__ import annotations

import pathlib
import argparse
import collections


def run(input_data: str) -> str:
    connections = [line.split("-") for line in input_data.strip().splitlines()]

    network = collections.defaultdict(list)
    for conn in connections:
        network[conn[0]].append(conn[1])
        network[conn[1]].append(conn[0])

    cliques = {(node,) for node in network}

    updated_cliques = set()
    for clique in cliques:
        new_clique = list(clique)
        for node in clique:
            for neighbor in network[node]:
                if neighbor not in new_clique and all(
                    neighbor in network[c_node] for c_node in new_clique
                ):
                    new_clique.append(neighbor)

        updated_cliques.add(tuple(sorted(new_clique)))

    largest_clique = max(updated_cliques, key=len)

    return ",".join(sorted(largest_clique))


def test_run(examples_dir: pathlib.Path) -> None:
    expected_answer = "co,de,ka,ta"

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
