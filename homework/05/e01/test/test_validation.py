import unittest

from util.validation import is_date

class TestValidation(unittest.TestCase):
    def test_is_date(self):
        self.assertTrue(is_date("2022-10-10"))
        self.assertTrue(is_date("2022-01-01"))
        self.assertTrue(is_date("5022-02-05"))
        self.assertFalse(is_date("2022-00-00"))
        self.assertFalse(is_date("2022-99-99"))
        self.assertFalse(is_date("2022-13-40"))
        self.assertFalse(is_date("0000-01-hj"))
        self.assertFalse(is_date("2hj2-01-20"))
        self.assertFalse(is_date("20232-10-12"))
