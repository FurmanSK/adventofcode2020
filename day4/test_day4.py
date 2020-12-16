# test day4.py

from day4 import Day4
from day4 import Passport
import pytest

testCase  = open('day4/testdata.txt', 'r')

@pytest.fixture
def tpuzzle():
    return Day4(testCase)

@pytest.fixture
def passport():
    pprt = Passport()
    pprt.hcl = "#88"
    pprt.ecl = "amb"
    pprt.byr = "1930"
    pprt.eyr = "1920"
    pprt.pid = "555333"
    pprt.hgt = "182cm"
    pprt.iyr = "2013"
    pprt.cid = "244"
    return pprt

def test_solve(tpuzzle):
    assert tpuzzle.solve() == 2

def test_class(tpuzzle):
    assert tpuzzle.puzzle == testCase

def test_check_if_valid(passport):
    assert passport.check_if_valid() == True
    passport.cid = ""
    assert passport.check_if_valid() == True
    passport.hcl = ""
    assert passport.check_if_valid() == False