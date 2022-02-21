import unittest

from validation import is_email

class TestEmail(unittest.TestCase):
    def test_is_email(self):
        self.assertTrue(is_email("jussi.pohjolainen@tuni.fi"))
        self.assertTrue(is_email("jussipohjolainen@tuni.fi"))
        self.assertTrue(is_email("jussi.pohjolainen@gov.uk.co"))
        self.assertTrue(is_email("Jussi.POhjolainen@Tuni.FI"))
        self.assertTrue(is_email("jussi.h.pohjolainen@tuni.fi"))
        self.assertTrue(is_email("sexy_beast69@hotmail78.com"))
        self.assertFalse(is_email("@tuni.fi"))
        self.assertFalse(is_email("hayhuh@@tuni.fi"))
        self.assertFalse(is_email("gduoiahdufip@"))
        self.assertFalse(is_email("dhjaihau@tuni."))