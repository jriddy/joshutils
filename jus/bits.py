"""Functions for dealing with bits."""


def bits(n):
    """Return the all the bits in the integer `n` from low to high"""
    if n == 0:
        yield 0
        return
    while n:
        yield n & 1
        n >>= 1
