# tests/test_complex_operations.py

import unittest
from calculator import (
    add_complex,
    subtract_complex,
    multiply_complex,
    divide_complex,
    conjugate_complex,
    modulus_complex,
    polar_complex,
    power_complex,
    sqrt_complex
)

class TestComplexOperations(unittest.TestCase):

    def test_add_complex_happy(self):
        self.assertEqual(add_complex(1 + 2j, 3 + 4j), 4 + 6j)

    def test_subtract_complex_happy(self):
        self.assertEqual(subtract_complex(5 + 6j, 2 + 3j), 3 + 3j)

    def test_multiply_complex_happy(self):
        self.assertEqual(multiply_complex(1 + 2j, 3 + 4j), -5 + 10j)

    def test_divide_complex_happy(self):
        self.assertEqual(divide_complex(1 + 2j, 3 + 4j), 0.44 + 0.08j)

    def test_conjugate_complex_happy(self):
        self.assertEqual(conjugate_complex(3 + 4j), 3 - 4j)

    def test_modulus_complex_happy(self):
        self.assertEqual(modulus_complex(3 + 4j), 5)

    def test_polar_complex_happy(self):
        self.assertEqual(polar_complex(3 + 4j), (5, 0.9272952180016122))

    def test_power_complex_happy(self):
        self.assertEqual(power_complex(1 + 1j, 2), 2j)

    def test_sqrt_complex_happy(self):
        self.assertEqual(sqrt_complex(3 + 4j), (2 + 1j))  # sqrt of 3 + 4i

    def test_add_complex_sad(self):
        with self.assertRaises(TypeError):
            add_complex(1, "2")

    def test_subtract_complex_sad(self):
        with self.assertRaises(TypeError):
            subtract_complex(1, None)

    def test_multiply_complex_sad(self):
        with self.assertRaises(TypeError):
            multiply_complex(1 + 2j, "3")

    def test_divide_complex_sad(self):
        with self.assertRaises(ZeroDivisionError):
            divide_complex(1 + 2j, 0)

    def test_power_complex_sad(self):
        with self.assertRaises(ValueError):
            power_complex(0, 0)

    def test_sqrt_complex_sad(self):
        with self.assertRaises(TypeError):
            sqrt_complex("test")

if __name__ == '__main__':
    unittest.main()
