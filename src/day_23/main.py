"""Day 23: LAN Party.

https://adventofcode.com/2024/day/23
"""

from __future__ import annotations

import collections

from pathlib import Path


cwd = Path(__file__).parent


def run_part_1(connections: list[list[str]]) -> int:
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


def run_part_2(connections: list[list[str]]) -> str:
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


def run(input_data: str) -> tuple[int, str]:
    connections = [line.split("-") for line in input_data.strip().splitlines()]

    part_1_answer = run_part_1(connections)
    part_2_answer = run_part_2(connections)

    return part_1_answer, part_2_answer


def test_run() -> None:
    expected_part_1_answer = 7
    expected_part_2_answer = "co,de,ka,ta"

    with (cwd / "example.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)

    assert (part_1_answer, part_2_answer) == (expected_part_1_answer, expected_part_2_answer)


if __name__ == "__main__":
    with (cwd / "input.txt").open() as file:
        input_data = file.read()

    part_1_answer, part_2_answer = run(input_data)
    print(part_1_answer, part_2_answer)
