__date__ = 'May 31, 2022'

import pytest


def find_max_sum(given: [int]) -> int | None:
    return None


@pytest.mark.parametrize("target,expected", [
    ([], None),  # Empty
    ([1, 2], 3),  # Just two
    ([1, 2, 3], 6),  # Simple
    ([1, 2, -3], 3),  # Simple with Negative
    ([1, -3, 1, -3, 1], -1),  # Two section are valid
])
def test_max_sum(target, expected):
    assert find_max_sum(target) == expected


if __name__ == '__main__':
    pytest.main()
