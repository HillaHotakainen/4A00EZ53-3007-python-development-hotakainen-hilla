import unittest

from main import reverse, isPalindrome

class TestMain(unittest.TestCase):
    def test_reverse(self):
        self.assertEqual(reverse("Kalle", lowercase=False), "ellaK")
        self.assertEqual(reverse("Kalle", lowercase=True), "ellak")
        self.assertEqual(reverse("Pulla", lowercase=True), "allup")
        self.assertEqual(reverse("Pallo", lowercase=False), "ollaP")

    def test_isPalindrome(self):
        self.assertEqual(isPalindrome("Saippuakauppias", lowercase=True), True)
        self.assertEqual(isPalindrome("Saippuakauppias", lowercase=False), False)
        self.assertEqual(isPalindrome("Kalle", lowercase=False), False)
        self.assertEqual(isPalindrome("Kalle", lowercase=True), False)