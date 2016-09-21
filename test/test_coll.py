import unittest

from jus import coll


class TestChunk(unittest.TestCase):

    def test_even(self):
        self.assertEqual(coll.chunk(range(4), 2), [(0, 1), (2, 3)])
