import unittest
from primeNumberSeries import prime_number_series


class Testing(unittest.TestCase):
    def test_one(self):
        self.assertEqual(prime_number_series(20),
                         [1, 2, 3, 5, 7, 11, 13, 17, 19])

    def test_two(self):
        self.assertEqual(prime_number_series(10), [1, 2, 3, 5, 7])

    def test_three(self):
        self.assertNotEqual(prime_number_series(50), [0, 1, 1, 2, 3, 5, 8])

    def test_four(self):
        self.assertNotEqual(prime_number_series(40), [0, 1, 3])

if __name__ == '__main__':
    unittest.main()

