# tests/test_statistics.py

import unittest
from calculator import mean, median, mode, standard_deviation

class TestStatisticsOperations(unittest.TestCase):

    # Happy scenarios for mean function
    def test_mean_happy(self):
        self.assertAlmostEqual(mean([1, 2, 3, 4, 5]), round(3, 2))                # Mean of [1, 2, 3, 4, 5] = 3
        self.assertAlmostEqual(mean([10, 20, 30]), round(20, 2))                  # Mean of [10, 20, 30] = 20
        self.assertAlmostEqual(mean([1.5, 2.5, 3.5]), round(2.5, 2))              # Mean of [1.5, 2.5, 3.5] = 2.5
        self.assertAlmostEqual(mean([-1, 0, 1]), round(0, 2))                     # Mean of [-1, 0, 1] = 0

    # Sad scenarios for mean function
    def test_mean_sad(self):
        with self.assertRaises(TypeError):
            mean("data")  # Type error for non-list input
        with self.assertRaises(ValueError):
            mean([])  # Value error for empty list
        with self.assertRaises(ValueError):
            mean([1, 2, 'a'])  # Value error for non-numeric elements

    # Happy scenarios for median function
    def test_median_happy(self):
        self.assertAlmostEqual(median([1, 3, 3, 6, 7, 8, 9]), round(6, 2))        # Median of [1, 3, 3, 6, 7, 8, 9] = 6
        self.assertAlmostEqual(median([1, 2, 3, 4]), round(2.5, 2))               # Median of [1, 2, 3, 4] = 2.5
        self.assertAlmostEqual(median([1.5, 2.5, 3.5]), round(2.5, 2))            # Median of [1.5, 2.5, 3.5] = 2.5

    # Sad scenarios for median function
    def test_median_sad(self):
        with self.assertRaises(TypeError):
            median("data")  # Type error for non-list input
        with self.assertRaises(ValueError):
            median([])  # Value error for empty list
        with self.assertRaises(ValueError):
            median([1, 2, 'a'])  # Value error for non-numeric elements

    # Happy scenarios for mode function
    def test_mode_happy(self):
        self.assertAlmostEqual(mode([1, 2, 3, 3, 4]), round(3, 2))                # Mode of [1, 2, 3, 3, 4] = 3
        self.assertAlmostEqual(mode([1, 1, 2, 2, 3]), round(1, 2))                # Mode of [1, 1, 2, 2, 3] = 1
        self.assertAlmostEqual(mode([1.5, 2.5, 2.5, 3.5]), round(2.5, 2))         # Mode of [1.5, 2.5, 2.5, 3.5] = 2.5

    # Sad scenarios for mode function
    def test_mode_sad(self):
        with self.assertRaises(TypeError):
            mode("data")  # Type error for non-list input
        with self.assertRaises(ValueError):
            mode([])  # Value error for empty list

    # Happy scenarios for standard_deviation function
    def test_standard_deviation_happy(self):
        self.assertAlmostEqual(standard_deviation([1, 2, 3, 4]), round(1.29, 2))  # Standard deviation of [1, 2, 3, 4]
        self.assertAlmostEqual(standard_deviation([10, 20, 30, 40]), round(12.91, 2))  # Standard deviation of [10, 20, 30, 40]

    # Sad scenarios for standard_deviation function
    def test_standard_deviation_sad(self):
        with self.assertRaises(ValueError):
            standard_deviation([])  # Value error for empty list
        with self.assertRaises(ValueError):
            standard_deviation([1])  # At least two data points required
        with self.assertRaises(TypeError):
            standard_deviation("data")  # Type error for non-list input
        with self.assertRaises(ValueError):
            standard_deviation([1, 2, 'a'])  # Value error for non-numeric elements

if __name__ == '__main__':
    unittest.main()
