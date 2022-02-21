import unittest

from validation import is_personal_id

class TestEmail(unittest.TestCase):
    def test_is_personal_id(self):
        self.assertTrue(is_personal_id("131052-308T"))
        self.assertTrue(is_personal_id("120464-121C"))
        self.assertTrue(is_personal_id("210202A841T"))
        self.assertTrue(is_personal_id("141280-513W"))
        self.assertFalse(is_personal_id("142080-513W"))
        self.assertFalse(is_personal_id("401280-513W"))
        self.assertFalse(is_personal_id("141280-9234"))
        self.assertFalse(is_personal_id("141280-513G"))
        self.assertFalse(is_personal_id("141280-513X"))
        self.assertFalse(is_personal_id("141hjk-513W"))
        self.assertFalse(is_personal_id("141280-ABCG"))
        self.assertFalse(is_personal_id("141280-9416"))