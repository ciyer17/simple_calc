# tests/test_trigonometry.py

import unittest
import math
from calculator import sin, cosine, tangent

class TestTrigonometricOperations(unittest.TestCase):

    # Happy scenarios for sine function
    def test_sin_happy(self):
        self.assertAlmostEqual(sin(0), 0)                             # sin(0) = 0
        self.assertAlmostEqual(sin(math.pi / 2), round(1, 2))        # sin(π/2) = 1
        self.assertAlmostEqual(sin(math.pi), round(0, 2))             # sin(π) = 0
        self.assertAlmostEqual(sin(3 * math.pi / 2), round(-1, 2))   # sin(3π/2) = -1

    # Sad scenarios for sine function
    def test_sin_sad(self):
        with self.assertRaises(TypeError):
            sin("90")  # Type error for non-numeric input
        with self.assertRaises(TypeError):
            sin(float('nan'))  # Type error for NaN input

    # Happy scenarios for cosine function
    def test_cosine_happy(self):
        self.assertAlmostEqual(cosine(0), round(1, 2))                 # cos(0) = 1
        self.assertAlmostEqual(cosine(math.pi / 2), round(0, 2))       # cos(π/2) = 0
        self.assertAlmostEqual(cosine(math.pi), round(-1, 2))           # cos(π) = -1
        self.assertAlmostEqual(cosine(3 * math.pi / 2), round(0, 2))   # cos(3π/2) = 0

    # Sad scenarios for cosine function
    def test_cosine_sad(self):
        with self.assertRaises(TypeError):
            cosine("90")  # Type error for non-numeric input
        with self.assertRaises(TypeError):
            cosine(float('nan'))  # Type error for NaN input

    # Happy scenarios for tangent function
    def test_tangent_happy(self):
        self.assertAlmostEqual(tangent(0), round(0, 2))               # tan(0) = 0
        self.assertAlmostEqual(tangent(math.pi / 4), round(1, 2))     # tan(π/4) = 1
        self.assertAlmostEqual(tangent(math.pi / 3), round(math.sqrt(3), 2))  # tan(π/3) = √3 ≈ 1.73
        self.assertAlmostEqual(tangent(-math.pi / 4), round(-1, 2))    # tan(-π/4) = -1

    # Sad scenarios for tangent function
    def test_tangent_sad(self):
        with self.assertRaises(ValueError):
            tangent(math.pi / 2)  # tan(π/2) is undefined
        with self.assertRaises(ValueError):
            tangent(3 * math.pi / 2)  # tan(3π/2) is undefined
        with self.assertRaises(TypeError):
            tangent("45")  # Type error for non-numeric input
        with self.assertRaises(TypeError):
            tangent(float('nan'))  # Type error for NaN input

if __name__ == '__main__':
    unittest.main()
