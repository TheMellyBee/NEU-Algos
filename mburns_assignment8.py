# author: Melanie Burns
# Due: July 21, 2022
# email: burns.me@northeasturn.edu
# StudentID: 002923383
# Base code given in assignment 6, but everything else is my own
from typing import Optional, Tuple, List

import pytest


class Graph:
    # i want to change this to take in the matrix and turn it into
    # a dict of list of connections
    def __init__(self, matrix: [[int]]):
        self.graph = {}
        for node_num, row in enumerate(matrix):
            for other_num, other_node in enumerate(row):
                if node_num == other_num:
                    continue

                if other_node == 1:
                    if node_num not in self.graph:
                        self.graph[node_num] = [other_num]
                    else:
                        self.graph[node_num].append(other_num)
        print(self.graph)

    def children(self, node) -> List[int]:
        if node not in self.graph:
            raise ValueError

        return self.graph[node]


def designate(g: Graph) -> Optional[Tuple[List[int]]]:
    return None


def countSimplePaths(g: Graph, s: int, t: int) -> int:
    count = 0
    visited = set()
    stack = g.children(s)

    while stack:
        node = stack.pop()
        if node == t:
            count += 1
            continue

        if node not in visited:
            visited.add(node)
            for child in g.children(node):
                stack.append(child)

    return count

@pytest.mark.parametrize("matrix,expected", [
    ([[0, 1], [1, 0]], ([0], [1])),
    ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], None)
])
def test_designate(matrix, expected):
    rivals = Graph(matrix)
    assert designate(rivals) == expected


@pytest.mark.parametrize("matrix,s,t,expected", [
    ([[0, 1], [1, 0]], 0, 1, 1),
    ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0, 2, 2)
])
def test_countSimplePaths(matrix, s, t, expected):
    graph = Graph(matrix)
    assert countSimplePaths(graph, s, t) == expected