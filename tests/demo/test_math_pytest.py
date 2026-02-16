import pytest
from math_utils import add, subtract, multiply, devide


def test_add_positive_numbers():
    """Test adding two positive numbers"""
    result = add(5, 3)
    assert result == 8

def test_add_negative_numbers():
    """Test adding two negative numbers"""
    assert add(-5, -3) == -8

def test_add_positive_negative_numbers():
    """Test adding positive and negative numbers"""
    assert add(5, -3) == 2
    assert add(-5, 3) == -2

# def test_subtract():
#     """Test subtraction"""
#     .assertEqual(subtract(5, 3), 2)
#     .assertEqual(subtract(20, 1), 19)
#     .assertEqual(subtract(5, 17), -12)
#     .assertEqual(subtract(9, -3), 12)

# def test_multiply():
#     """Test multiply"""
#     .assertEqual(multiply(5, 3), 15)
#     .assertEqual(multiply(20, 1), 20)

def test_devide():
    """Test division"""
    # .assertEqual(devide(15, 3), 5)
    # .assertEqual(devide(-20, 2), -10)
    with pytest.raises(ValueError):
        devide(10,0)
    with pytest.raises(ValueError, match="error devide by zero"):
        devide(10,0)

if __name__ == "__main__":
    main()