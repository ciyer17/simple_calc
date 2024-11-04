# tests/test_basic_operations.py

import unittest
from calculator import * 

class TestBasicOperations(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(1.5, 2.5), 4.0)
        self.assertEqual(add(1e10, 1e10), 2e10)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(2.5, 1.5), 1.0)
        self.assertEqual(subtract(1e10, 1e10), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(1.5, 2), 3.0)
        self.assertEqual(multiply(1e10, 2), 2e10)
        self.assertEqual(multiply(0, 1e10), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(1, -1), -1)
        self.assertEqual(divide(5.0, 2), 2.5)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)
        with self.assertRaises(TypeError):
            divide(10, 'a')

if __name__ == '__main__':
    unittest.main()
