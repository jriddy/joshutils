import unittest

from jus import coll


class TestChunk(unittest.TestCase):

    def test_even(self):
        self.assertEqual(coll.chunk(range(4), 2), [(0, 1), (2, 3)])

    def test_odd(self):
        self.assertEqual(coll.chunk(range(5), 2), [(0, 1), (2, 3)])

    def test_type_error(self):
        self.assertRaises(TypeError, coll.chunk, range(10), 1.0)
