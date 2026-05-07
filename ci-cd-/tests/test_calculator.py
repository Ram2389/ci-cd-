from calculator.calculator import add, subtract, multiply, divide
import pytest

def test_add():
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply(3, 3) == 9
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(0, 1) == 0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
