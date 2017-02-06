import unittest
from ipValidation import ip_validation


class Testing(unittest.TestCase):
    def test_one(self):
        self.assertEqual(ip_validation('192.168.0.1'), 'Valid IP')

    def test_two(self):
        self.assertEqual(ip_validation('1.1.1.1'), 'Valid IP')

    def test_three(self):
        self.assertEqual(ip_validation('!@#%^&*'), 'Invalid IP')

    def test_four(self):
        self.assertEqual(ip_validation('!sxs.123.123.123'), 'Invalid IP')

if __name__ == '__main__':
    unittest.main()

