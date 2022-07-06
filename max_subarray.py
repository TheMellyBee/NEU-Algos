__date__ = 'May 31, 2022'
__author__ = "Melly Burns" # Student ID 002923383

import pytest


def linear_max_sum(given: [int]) -> int | None:
    if not given or len(given) == 0:
        return None

    max_sum = given[0]
    current_window = given[0]

    for item in given[1:]:
        current_window += item
        if current_window < 0:
            current_window = item
        if current_window > max_sum:
            max_sum = current_window

    return max_sum


@pytest.mark.parametrize("target,expected", [
    ([], None),  # Empty
    ([1, 2], 3),  # Just two
    ([1, 2, 3], 6),  # Simple
    ([1, 2, -3], 3),  # Simple with Negative
    ([1, -3, 1], 1),  # Two section are valid
    ([-3, -4, -1], -1),
    ([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7], 43)
])
def test_max_sum(target, expected):
    assert linear_max_sum(target) == expected


if __name__ == '__main__':
    pytest.main()
