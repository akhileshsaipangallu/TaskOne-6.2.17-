import sys
import unittest
from b import read_nth_line


class Testing(unittest.TestCase):

    def test_one(self):
        line = 'Donate link: http://example.com/\n'
        self.assertEqual(read_nth_line(5, sys.argv[1]), line)

if __name__ == '__main__':
    unittest.main(argv=[sys.argv[1]])

