import unittest
from phoneNumberValidation import phone_number_validation


class Testing(unittest.TestCase):
    def test_one(self):
        self.assertEqual(phone_number_validation('9874561230'),
                         'Valid phone number')

    def test_two(self):
        self.assertEqual(phone_number_validation('8529637410'),
                         'Valid phone number')

    def test_three(self):
        self.assertEqual(phone_number_validation('123123'),
                         'Invalid phone number')

    def test_four(self):
        self.assertEqual(phone_number_validation('xfgh'),
                         'Invalid phone number')

if __name__ == '__main__':
    unittest.main()

