# tests/test_logarithms.py

import unittest
import math
import sys
from calculator import logarithm, natural_log, exponential

class TestMathOperations(unittest.TestCase):
    
    # Happy scenarios for logarithm function
    def test_logarithm_happy(self):
        self.assertAlmostEqual(logarithm(8, 2), 3)                   # log2(8) = 3
        self.assertAlmostEqual(logarithm(100, 10), 2)                # log10(100) = 2
        self.assertAlmostEqual(logarithm(math.e, math.e), 1)         # loge(e) = 1
        self.assertAlmostEqual(logarithm(float('inf'), 2), float('inf'))  # log2(inf) = inf
        self.assertAlmostEqual(logarithm(1, 10), 0)                   # log10(1) = 0

    # Sad scenarios for logarithm function
    def test_logarithm_sad(self):
        with self.assertRaises(ValueError):
            logarithm(0, 10)  # Logarithm of zero is undefined
        with self.assertRaises(ValueError):
            logarithm(-1, 10)  # Logarithm of a negative number is undefined
        with self.assertRaises(ValueError):
            logarithm(10, -1)  # Logarithm base cannot be negative
        with self.assertRaises(TypeError):
            logarithm("8", 2)  # Type error for non-numeric input
        with self.assertRaises(ValueError):
            logarithm(float('-inf'), 10)  # Logarithm for negative infinity is undefined

    # Happy scenarios for natural_log function
    def test_natural_log_happy(self):
        self.assertAlmostEqual(natural_log(1), 0)                     # ln(1) = 0
        self.assertAlmostEqual(natural_log(math.e), 1)                # ln(e) = 1
        self.assertAlmostEqual(natural_log(math.e**2), 2)             # ln(e^2) = 2

    # Sad scenarios for natural_log function
    def test_natural_log_sad(self):
        with self.assertRaises(ValueError):
            natural_log(0)  # Natural log of zero is undefined
        with self.assertRaises(ValueError):
            natural_log(-1)  # Natural log of a negative number is undefined
        with self.assertRaises(TypeError):
            natural_log("e")  # Type error for non-numeric input
        with self.assertRaises(ValueError):
            natural_log(float('-inf'))  # Natural log for negative infinity is undefined

    # Happy scenarios for exponential function
    def test_exponential_happy(self):
        self.assertAlmostEqual(exponential(0), 1)                      # e^0 = 1
        self.assertAlmostEqual(exponential(1), round(math.e, 2))                 # e^1 = e
        self.assertAlmostEqual(exponential(2), round(math.e**2, 2))              # e^2 = e^2
        self.assertAlmostEqual(exponential(float('-inf')), 0.0)       # e^(-inf) = 0.0

    # Sad scenarios for exponential function
    def test_exponential_sad(self):
        with self.assertRaises(TypeError):
            exponential("2")  # Type error for non-numeric input
        with self.assertRaises(OverflowError):
            exponential(math.log(sys.float_info.max) + 1)  # Overflow for large input

if __name__ == '__main__':
    unittest.main()
