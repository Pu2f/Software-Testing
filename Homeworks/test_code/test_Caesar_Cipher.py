from code_under_test.Caesar_Cipher import caesarCipher
import unittest
class TestCaesarCipher(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(caesarCipher("middle-Outz", 2), "okffng-Qwvb")