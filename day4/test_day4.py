# test day4.py

from day4 import Day4
from day4 import Passport
import pytest

testCase  = open('day4/testdata.txt', 'r')
testCase2  = open('day4/testdata2.txt', 'r')

@pytest.fixture
def tpuzzle():
    return Day4(testCase)

@pytest.fixture
def tpuzzle2():
    return Day4(testCase2)

@pytest.fixture
def passport():
    pprt = Passport()
    pprt.hcl = "#885577"
    pprt.ecl = "amb"
    pprt.byr = "1930"
    pprt.eyr = "2021"
    pprt.pid = "022111849"
    pprt.hgt = "182cm"
    pprt.iyr = "2013"
    pprt.cid = "244"
    return pprt

def test_solve(tpuzzle):
    # test part 1
    ret = tpuzzle.solve()[1]
    assert ret == 2

def test_solve_p2(tpuzzle2):
    # test part 1
    ret = tpuzzle2.solve()[1]
    assert ret == 4

def test_class(tpuzzle):
    assert tpuzzle.puzzle == testCase

def test_check_if_valid_p1(passport):
    assert passport.check_if_valid_p1() == True
    passport.cid = ""
    assert passport.check_if_valid_p1() == True
    passport.hcl = ""
    assert passport.check_if_valid_p1() == False

def test_check_if_valid_p2(passport):
    assert passport.check_if_valid_p2() == True
    passport.cid = ""
    assert passport.check_if_valid_p2() == True
    passport.hcl = ""
    assert passport.check_if_valid_p2() == False

def test_check_hgt(passport):
    passport.hgt = "199cm"
    assert passport.check_hgt() == False
    passport.hgt = "190cm"
    assert passport.check_hgt() == True
    passport.hgt = "80in"
    assert passport.check_hgt() == False
    passport.hgt = "60in"
    assert passport.check_hgt() == True

def test_check_hcl(passport):
    assert bool(passport.check_hcl()) == True
    passport.hcl = "#88"
    assert bool(passport.check_hcl()) == False

def test_check_ecl(passport):
    assert passport.check_ecl() == True
    passport.ecl = "aaa"
    assert passport.check_ecl() == False

def test_check_pid(passport):
    assert bool(passport.check_pid()) == True
    passport.pid = "000"
    assert bool(passport.check_pid()) == False