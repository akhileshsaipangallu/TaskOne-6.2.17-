import unittest
from wordCount import word_count


class Testing(unittest.TestCase):
    def test_one(self):
        self.assertEqual(word_count('up'), 1)

    def test_two(self):
        self.assertEqual(word_count('above'), 6)

    def test_three(self):
        self.assertNotEqual(word_count('ok'), 5)

    def test_four(self):
        self.assertNotEqual(word_count('and'), 9)

if __name__ == '__main__':
    unittest.main()

