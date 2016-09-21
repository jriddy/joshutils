import unittest

from jus import bits


class TestBits(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(list(bits.bits(0)), [0])

    def test_one(self):
        self.assertEqual(list(bits.bits(1)), [1])

    def test_full_byte(self):
        self.assertEqual(list(bits.bits(0xFF)), [1] * 8)

    def test_alternating(self):
        self.assertEqual(list(bits.bits(0b1010110)),
                         list(reversed([1, 0, 1, 0, 1, 1, 0])))
