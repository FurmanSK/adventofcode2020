

from day5 import Day5

import pytest

@pytest.mark.parametrize("boardingpass, expected", [
    ("BFFFBBFRRR", 567),
    ("FFFBBBFRRR", 119),
    ("BBFFBBFRLL", 820)
])
def test_parse_boarding_pass(boardingpass, expected):
    bp = Day5(boardingpass)
    assert bp.parse_boarding_pass(boardingpass) == expected