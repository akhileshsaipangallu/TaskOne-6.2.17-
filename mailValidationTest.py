import unittest
from mailValidation import mail_validation


class Testing(unittest.TestCase):
    def test_one(self):
        self.assertEqual(mail_validation('akh@gmail.com'), 'Valid mailID')

    def test_two(self):
        self.assertEqual(mail_validation('ak123@tarams.com'), 'Valid mailID')

    def test_three(self):
        self.assertEqual(mail_validation('123@123.!@#'), 'Invalid mailID')

    def test_four(self):
        self.assertEqual(mail_validation('!@#$@!@#.!@#'), 'Invalid mailID')

if __name__ == '__main__':
    unittest.main()

