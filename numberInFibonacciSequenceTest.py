import unittest
from c import check_series, series


class Testing(unittest.TestCase):
    def test_one(self):
        self.assertTrue(check_series(1, 1, 8))

    def test_two(self):
        self.assertFalse(check_series(1, 1, 35))

    def test_three(self):
        self.assertFalse(check_series(1, 1, 9))

    def test_four(self):
        self.assertTrue(check_series(1, 1, 13))

if __name__ == '__main__':
    unittest.main()
