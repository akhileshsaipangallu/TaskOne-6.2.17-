import unittest
from numberValidation import number_validation


class Testing(unittest.TestCase):
    def test_one(self):
        self.assertEqual(number_validation('1231321'), 'Valid number')

    def test_two(self):
        self.assertEqual(number_validation('684654411'), 'Valid number')

    def test_three(self):
        self.assertEqual(number_validation('123@123'), 'Invalid number')

    def test_four(self):
        self.assertEqual(number_validation('xfgh'), 'Invalid number')

if __name__ == '__main__':
    unittest.main()

