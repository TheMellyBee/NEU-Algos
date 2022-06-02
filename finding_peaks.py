__date__ = 'May 31, 2022'
__author__ = "Melly Burns" # Student ID 002923383

import pytest


def finding_peaks(given: [int]) -> int | None:
    if not given or len(given) == 0:
        return None
    if len(given) == 1:
        return 0

    for index, item in enumerate(given):
        if index == 0 and item > given[index + 1]:
            return index
        elif index == len(given) - 1 and item > given[index - 1]:
            return index
        elif item > given[index - 1] and item > given[index + 1]:
            return index

    return None


@pytest.mark.parametrize("target,expected", [
    ([], None),         # Empty
    ([2, 1], [0]),        # Left Peak
    ([1, 2], [1]),        # Right Peak
    ([1, 2, 1], [1]),        # Middle peak
    ([-1, -2], [0]),     # middle with negative
    ([-2, 1, -2, 3], [1, 3]),   # multiple peaks (should grab the first
    ([1, 1, 1], None),  # no peaks
    ([7, 2, 6, 4, 9, 8, 5, 3, 1], [0, 2, 4])
])
def test_finding_peaks(target, expected):
    result = finding_peaks(target)

    if result is None:
        assert result == expected
    else:
        assert result in expected


if __name__ == '__main__':
    pytest.main()
