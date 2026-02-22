from code_under_test.Alternating_Characters import alternatingCharacters
import unittest

class TestAlternatingCharacters(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
        self.assertEqual(alternatingCharacters("BBBBB"), 4)
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
        self.assertEqual(alternatingCharacters("BABABA"), 0)
        self.assertEqual(alternatingCharacters("AAABBB"), 4)