import unittest
from code_under_test.Funny_String import funnystring
class TestFunnyString(unittest.TestCase):
    def test_case_0(self):
        # Arrange
        stdin = "Puff"
        stdin2 = "abc"
        # Act
        result = funnystring(stdin)
        result2 = funnystring(stdin2)
        # Assert
        self.assertEqual(result, "Not Funny")
        self.assertEqual(result2, "Funny")