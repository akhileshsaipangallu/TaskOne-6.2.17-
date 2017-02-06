import unittest
from primeNumber import prime_checking


class Testing(unittest.TestCase):

    def test_one(self):
        self.assertTrue(prime_checking(5))

    def test_two(self):
        self.assertFalse(prime_checking(6))

    def test_three(self):
        self.assertFalse(prime_checking(0))

if __name__ == '__main__':
    unittest.main()

