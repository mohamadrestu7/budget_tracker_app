import unittest
from math_utils import add, subtract, multiply, devide

class TestMathUtils(unittest.TestCase):
    def test_add_positive_numbers(self):
        """Test adding two positive numbers"""
        result = add(5, 3)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        """Test adding two negative numbers"""
        self.assertEqual(add(-5, -3), -8)

    def test_add_positive_negative_numbers(self):
        """Test adding positive and negative numbers"""
        self.assertEqual(add(5, -3), 2)
        self.assertEqual(add(-5, 3), -2)

    def test_subtract(self):
        """Test subtraction"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(20, 1), 19)
        self.assertEqual(subtract(5, 17), -12)
        self.assertEqual(subtract(9, -3), 12)

    def test_multiply(self):
        """Test multiply"""
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(20, 1), 20)

    def test_devide(self):
        """Test division"""
        self.assertEqual(devide(15, 3), 5)
        self.assertEqual(devide(-20, 2), -10)
        with self.assertRaises(ValueError):
            devide(10,0)

if __name__ == "__main__":
    unittest.main()