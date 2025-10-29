# David Wylie
# CIS256 Fall 2025
# Programming Assignment 4.1 (PA 4)
# Testing Suite for Calculator Program

import pytest
from Programming_4_Calculator_David_Wylie import (
    add,
    subtract,
    multiply,
    divide,
)


def test_add():
    """
    Tests the add function with various number combinations.
    Validates positive, negative, zero, and large numbers.
    Uses pytest.approx() for floating point precision.
    """
    assert add(2.0, 3.0) == 5.0
    assert add(0.0, 3.0) == 3.0
    assert add(1000000000.0, 3.0) == 1000000003.0
    assert add(2.0, -3.0) == -1.0
    assert add(0.0, -3.0) == -3.0
    assert add(-2.0, -3.0) == -5.0
    assert add(0.0, 0.0) == 0.0
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_subtract():
    """
    Tests the subtract function with various number combinations.
    Validates positive, negative, zero, and large numbers.
    Uses pytest.approx() for floating point precision.
    """
    assert subtract(5.0, 3.0) == 2.0
    assert subtract(2.0, 3.0) == -1.0
    assert subtract(0.0, 3.0) == -3.0
    assert subtract(1000000003.0, 3.0) == 1000000000.0
    assert subtract(2.0, -3.0) == 5.0
    assert subtract(0.0, -3.0) == 3.0
    assert subtract(-2.0, -3.0) == 1.0
    assert subtract(0.0, 0.0) == 0.0
    assert subtract(0.3, 0.2) == pytest.approx(0.1)


def test_multiply():
    """
    Tests the multiply function with various number combinations.
    Validates positive, negative, zero, and large numbers.
    Uses pytest.approx() for floating point precision.
    """
    assert multiply(5.0, 3.0) == 15.0
    assert multiply(2.0, 3.0) == 6.0
    assert multiply(0.0, 3.0) == 0.0
    assert multiply(1000000000.0, 3.0) == 3000000000.0
    assert multiply(2.0, -3.0) == -6.0
    assert multiply(0.0, -3.0) == 0.0
    assert multiply(-2.0, -3.0) == 6.0
    assert multiply(0.0, 0.0) == 0.0
    assert multiply(0.3, 0.2) == pytest.approx(0.06)


def test_divide():
    """
    Tests the divide function with various number combinations.
    Validates positive, negative, zero, and large numbers.
    Uses pytest.approx() for floating point precision.
    Verifies ZeroDivisionError is raised when dividing by zero.
    """
    assert divide(45.0, 3.0) == 15.0
    assert divide(12.0, 3.0) == 4.0
    assert divide(0.0, 3.0) == 0.0
    assert divide(3000000000.0, 3.0) == 1000000000.0
    assert divide(10.0, -5.0) == -2.0
    assert divide(0.0, -3.0) == 0.0
    assert divide(-6.0, -3.0) == 2.0
    assert divide(0.06, 0.2) == pytest.approx(0.3)
    with pytest.raises(ZeroDivisionError):
        divide(5.0, 0.0)
