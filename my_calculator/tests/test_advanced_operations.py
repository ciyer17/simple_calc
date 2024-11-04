# tests/test_advanced_operations.py

import unittest
from calculator import power, square_root, factorial

class TestMathOperations(unittest.TestCase):
    
    # Happy scenarios for power function
    def test_power_happy(self):
        self.assertEqual(power(2, 3), 8)           # 2^3 = 8
        self.assertEqual(power(5, 0), 1)           # 5^0 = 1
        self.assertEqual(power(0, 5), 0)           # 0^5 = 0
        self.assertEqual(power(2, -2), 0.25)       # 2^(-2) = 0.25
        self.assertEqual(power(2, float('inf')), float('inf'))  # 2^(inf) = inf

    # Sad scenarios for power function
    def test_power_sad(self):
        with self.assertRaises(TypeError):
            power("2", 3)  # Type error for string input
        with self.assertRaises(ZeroDivisionError):
            power(0, -1)   # 0 raised to a negative exponent
        with self.assertRaises(ValueError):
            power(0, 0)    # 0^0 is undefined
        with self.assertRaises(ValueError):
            power(float('-inf'), float('inf'))  # Negative inf raised to positive inf

    # Happy scenarios for square_root function
    def test_square_root_happy(self):
        self.assertEqual(square_root(4), 2)         # √4 = 2
        self.assertEqual(square_root(0), 0.0)       # √0 = 0
        self.assertEqual(square_root(9), 3)         # √9 = 3
        self.assertEqual(square_root(2), 1.41)      # √2 ≈ 1.41 rounded to 2 decimals
        self.assertEqual(square_root(float('inf')), float('inf'))  # √inf = inf

    # Sad scenarios for square_root function
    def test_square_root_sad(self):
        with self.assertRaises(ValueError):
            square_root(-1)  # Cannot compute square root of negative
        with self.assertRaises(TypeError):
            square_root("4")  # Type error for string input
        with self.assertRaises(ValueError):
            square_root(float('-inf'))  # Cannot compute sqrt of negative infinity

    # Happy scenarios for factorial function
    def test_factorial_happy(self):
        self.assertEqual(factorial(5), 120)         # 5! = 120
        self.assertEqual(factorial(0), 1)           # 0! = 1
        self.assertEqual(factorial(1), 1)           # 1! = 1
        self.assertEqual(factorial(3), 6)           # 3! = 6

    # Sad scenarios for factorial function
    def test_factorial_sad(self):
        with self.assertRaises(ValueError):
            factorial(-1)  # Factorial is not defined for negative numbers
        with self.assertRaises(TypeError):
            factorial(2.5)  # Type error for float input
        with self.assertRaises(OverflowError):
            factorial(1000)  # High value might lead to overflow

if __name__ == '__main__':
    unittest.main()
