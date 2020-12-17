
from day6 import Day6

import pytest

@pytest.mark.parametrize("customs_ans, expected", [
    (["abc\n", '\n'], 3),
    (["a\n", "b\n", "c\n", '\n'], 3),
    (["ab\n", "ac\n", '\n'], 3),
])
def test_parse_boarding_pass(customs_ans, expected):
    # this is testing counting YES answers per one group
    bp = Day6(customs_ans)
    ret = bp.parse_customs_forms()
    assert ret[0] == expected

@pytest.mark.parametrize("customs_ans, expected", [
    (["abc\n", '\n'], 3),
    (["a\n", "b\n", "c\n", '\n'], 0),
    (["ab\n", "ac\n", '\n'], 1),
])
def test_parse_boarding_pass(customs_ans, expected):
    # this is testing counting YES answers per one group
    bp = Day6(customs_ans)
    ret = bp.parse_customs_forms()
    assert ret[1] == expected