import unittest
from code_under_test.Grid_Challenge import gridChallenge
class TestGridChallenge(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(gridChallenge(["abc", "ade", "efg"]), "YES")
        self.assertEqual(gridChallenge(["abc", "hjk", "mpq", "rtv"]), "YES")
        self.assertEqual(gridChallenge(["mpxz", "abcd", "wlmf"]), "NO")