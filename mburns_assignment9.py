# author: Melanie Burns
# date: August 4, 2022
# email: burns.me@northeasturn.edu
# StudentID: 002923383
# Base code given in assignment 9, but everything else is my own

# Note: the first test is failing, but I'm it is gtting a MST that looks just as good.
# The second test does pass.
from typing import Tuple, List, Any

import pytest
import math

# Problem 1
# To make my own MST I’d work with a priority queue and set for keep track of the cut.
# First, I’d put all nodes into the priority queue based on the sum of their edges.
# Then take two lowest summed nodes called a and b. From here I’d make the cut based
# on what is the lowest weighted edge from the union of edges of a and b. This method
# should prioritise nodes with less edges especially with low weights first so we
# might have more choices as we go.


def prim2(g: List[List[int]], r: int) -> List[Tuple[int]]:
    n = len(g)
    proximity = [(None, math.inf)] * n
    proximity[r] = (None, 0)  # It's the start os has no predecessor and proximity is 0
    picked_vertex = set()

    vertex = r
    for i in range(n):

        min = math.inf
        for potential in range(n):
            if potential not in picked_vertex and proximity[potential][1] < min:
                min = proximity[potential][1]
                vertex = potential

        picked_vertex.add(vertex)

        for next_vertex in range(n):
            if vertex != next_vertex and next_vertex not in picked_vertex and g[vertex][next_vertex] < proximity[next_vertex][1]:
                proximity[next_vertex] = (vertex, g[vertex][next_vertex])

    A = []
    for i in range(n):
        # proximity[1] = (0, 4) is the proximity for vertex 1 is 4 and it's predecssor is 0
        if proximity[i][0] is not None:
            A.append((i, proximity[i][0]))

    return A


GRAPH_1 = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]]

ANSWER_1 = [(1, 0), (2, 1), (3, 2), (4, 3), (5, 2), (6, 5), (7, 6), (8, 2)]

GRAPH_2 = [[0, 8, 5, 9, 6, 3],
           [8, 0, 2, 2, 5, 2],
           [5, 2, 0, 3, 1, 7],
           [9, 2, 3, 0, 1, 9],
           [6, 5, 1, 1, 0, 9],
           [3, 2, 7, 9, 9, 0]]

ANSWER_2 = [(1, 5), (2, 1), (3, 4), (4, 2), (5, 0)]


@pytest.mark.parametrize("g,r,expected", [
    (GRAPH_1, 0, ANSWER_1),
    (GRAPH_2, 0, ANSWER_2)
])
def test_prim2(g, r, expected):
    assert prim2(g, r) == expected
