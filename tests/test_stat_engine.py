import unittest
import sys
import os

# Adds the 'src' folder to the search path - NO SPACES BEFORE THIS LINE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from stat_engine import StatEngine

class TestStatEngine(unittest.TestCase):

    def test_median_odd(self):
        engine = StatEngine([1, 3, 5])
        self.assertEqual(engine.get_median(), 3.0)

    def test_median_even(self):
        engine = StatEngine([1, 2, 3, 4])
        self.assertEqual(engine.get_median(), 2.5)

    def test_empty_list(self):
        # We wrap the initialization in 'assertRaises' 
        # because the error happens the moment you create StatEngine([])
        with self.assertRaises(ValueError):
            StatEngine([])
    def test_standard_deviation(self):
        engine = StatEngine([10, 20])
        self.assertAlmostEqual(engine.get_standard_deviation(), 7.071, places=3)

    def test_outlier_detection(self):
        # We use a very extreme value (1000) to ensure it's caught as an outlier
        engine = StatEngine([1, 2, 3, 1000])
        outliers = engine.get_outliers(threshold=1) 
        self.assertIn(1000, outliers)

if __name__ == '__main__':
    unittest.main()