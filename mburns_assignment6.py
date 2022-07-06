# author: Melanie Burns
# Due: July 5, 2022
# email: burns.me@northeasturn.edu
# StudentID: 002923383
# Base code given in assignment 6, but everything else is my own
import pytest


def minimal_removal(tasks: list[tuple[int, int]]) -> int:
    pass


def minAvgCompletion1(tasks: list[int]) -> float:
    pass


def minAvgCompletion2(tasks: list[list[int]]) -> float:
    pass


@pytest.mark.parametrize("tasks,expected", [
    ([(0, 1), (0, 1), (0, 1)], 2),
    ([(0, 1), (1, 2)], 0)
])
def test_minimal_removal(tasks: list[tuple[int, int]], expected: int):
    assert minimal_removal(tasks, expected)


@pytest.mark.parametrize("tasks,expected", [
    ([3, 5], 2)
])
def test_minAvgCompletion1(tasks: list[int], expected: float):
    assert minAvgCompletion1(tasks) == expected


@pytest.mark.parametrize("tasks,expected", [
    ([[3, 5], [5, 2]], 8.5),
    ([[3, 5], [5, 4]], 10.0)
])
def test_minAvgCompletion2(tasks: list[list[int]], expected: float):
    assert minAvgCompletion2(tasks) == expected


if __name__ == '__main__':
    pytest.main()