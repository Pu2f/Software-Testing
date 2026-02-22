import unittest
from code_under_test.Two_Characters import alternate

class TestTwoCharacters(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(alternate("beabeefeab"), 5)