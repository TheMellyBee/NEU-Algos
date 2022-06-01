__date__ = 'May 31, 2022'

import pytest


def finding_peaks(given: [int]) -> int | None:
    return None


@pytest.mark.parametrize("target,expected", [
    ([], None),         # Empty
    ([2, 1], 2),        # Left Peak
    ([1, 2], 2),        # Right Peak
    ([1, 2, 1]),        # Middle peak
    ([-1, -2], -1),     # middle with negative
    ([-2, 1, -2, 3]),   # multiple peaks (should grab the first
    ([1, 1, 1], None),  # no peaks
])
def test_finding_peaks(target, expected):
    assert finding_peaks(target) == expected

if __name__ == '__main__':
    pytest.main()
