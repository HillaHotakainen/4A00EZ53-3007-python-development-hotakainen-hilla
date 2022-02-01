import unittest

def calculate_sum (no1, no2):
    return no1 + no2

class TestMain(unittest.TestCase):
    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(4, 4), 8)
        self.assertEqual(calculate_sum(-4, 4), 0)
        self.assertEqual(calculate_sum(-2, -2), -4)
        self.assertEqual(calculate_sum(0, 0), 0)
        self.assertEqual(calculate_sum(1, 2), 3)