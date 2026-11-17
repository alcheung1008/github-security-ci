import pytest

from sample_code import add, subtract, multiply, divide


def test_add():
    """Verify that addition returns correct results."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(1.5, 1.5) == 3.0


def test_subtract():
    """Verify that subtraction returns correct results."""
    assert subtract(10, 5) == 5
    assert subtract(-1, -1) == 0


def test_multiply():
    """Verify that multiplication returns correct results."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 2) == -4


def test_divide():
    """Verify division and division-by-zero handling."""
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

    with pytest.raises(ValueError):
        divide(10, 0)