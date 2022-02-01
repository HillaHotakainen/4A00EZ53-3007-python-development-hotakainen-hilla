
import unittest

from main import calculate_sum, get_max

class TestMain(unittest.TestCase):
    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(4, 4), 8)
        self.assertEqual(calculate_sum(-4, 4), 0)
        self.assertEqual(calculate_sum(-2, -2), -4)
        self.assertEqual(calculate_sum(0, 0), 0)
        self.assertEqual(calculate_sum(1, 2), 3)

    def test_get_max(self):
        self.assertEqual(get_max(1, 2, 3), 3)
        self.assertEqual(get_max(1, 5, 2), 5)
        self.assertEqual(get_max(-1, 0, 1), 1)
        self.assertEqual(get_max(-1, -2, -3), -1)
        self.assertEqual(get_max(10, 50, -25), 50)