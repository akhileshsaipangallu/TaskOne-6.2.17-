import unittest
from specialCharValidation import special_char_validation


class Testing(unittest.TestCase):
    def test_one(self):
        self.assertEqual(special_char_validation('&&&&&--'),
                         'Valid special character/characters')

    def test_two(self):
        self.assertEqual(special_char_validation('&-()'),
                         'Valid special character/characters')

    def test_three(self):
        self.assertEqual(special_char_validation('123123'),
                         'Invalid special character/characters')

    def test_four(self):
        self.assertEqual(special_char_validation('xfgh'),
                         'Invalid special character/characters')

if __name__ == '__main__':
    unittest.main()

