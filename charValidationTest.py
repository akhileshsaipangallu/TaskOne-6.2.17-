import unittest
from charValidation import char_validation


class Testing(unittest.TestCase):
    def test_one(self):
        self.assertEqual(char_validation('ascascascac'),
                         'Valid character/characters')

    def test_two(self):
        self.assertEqual(char_validation('scasca51'),
                         'Invalid character/characters')

    def test_three(self):
        self.assertEqual(char_validation('!@#%^&*'),
                         'Invalid character/characters')

    def test_four(self):
        self.assertEqual(char_validation('!sxsaxasx'),
                         'Invalid character/characters')

if __name__ == '__main__':
    unittest.main()

