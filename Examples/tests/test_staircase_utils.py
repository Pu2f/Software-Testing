import unittest
from Staircase.staircase_utils import staircase


class TestStaircase(unittest.TestCase):

    def test_basic_case(self):
        # Arrange
        n = 4
        ch = "#"
        expected = "   #\n  ##\n ###\n####"

        # Act
        result = staircase(n, ch)

        # Assert
        self.assertEqual(result, expected)


    def test_invalid_n(self):
        # Arrange
        n = 0
        ch = "#"

        # Act / Assert
        with self.assertRaises(ValueError):
            staircase(n, ch)


    def test_custom_character(self):
        # Arrange
        n = 3
        ch = "*"
        expected = "  *\n **\n***"

        # Act
        result = staircase(n, ch)

        # Assert
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()