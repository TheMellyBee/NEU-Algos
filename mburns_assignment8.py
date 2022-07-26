# author: Melanie Burns
# Due: July 21, 2022
# email: burns.me@northeasturn.edu
# StudentID: 002923383
# Base code given in assignment 6, but everything else is my own
from typing import Optional, Tuple, List

import pytest


class Graph:
    def __init__(self, matrix: [[int]]):
        self.matrix = matrix
        self.num_rows = len(matrix)
        self.num_columns = len(matrix[0])

    def _is_valid_cell(self, x: int, y: int) -> bool:
        if  0 <= x < self.num_rows and 0 <= y < self.num_rows:
            return True
        return False

    def children(self, x: int, y:int) -> List[Tuple[int]]:
        pass

def designate(g: Graph) -> Optional[Tuple[List[int]]]:
    return None


def countSimplePaths(g: Graph, s: int, t: int) -> int:
    count = 0

    return count


@pytest.mark.parametrize("matrix,expected", [
    ([[0, 1], [1, 0]], ([0], [1])),
    ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], None)
])
def test_designate(matrix, expected):
    rivals = Graph(matrix)
    assert designate(g) == expected


@pytest.mark.parametrize("matrix,s,t,expected", [
    ([[0, 1], [1, 0]], 0, 1, 1),
    ([[0, 1, 1], [1, 0, 1], [1, 1, 0]], 0, 2, 2)
])
def test_countSimplePaths(matrix, s, t, expected):
    rivals = Graph(matrix)
    assert designate(g) == expected