import unittest
from FibonacciSequence import series


class Testing(unittest.TestCase):
    def test_one(self):
        self.assertEqual(series(14), [0, 1, 1, 2, 3, 5, 8, 13])

    def test_two(self):
        self.assertEqual(series(8), [0, 1, 1, 2, 3, 5, 8])

    def test_three(self):
        self.assertNotEqual(series(50), [0, 1, 1, 2, 3, 5, 8])

    def test_four(self):
        self.assertNotEqual(series(40), [0, 1, 3])

if __name__ == '__main__':
    unittest.main()

