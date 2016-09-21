"""Module providing utilites for operating on collections.

Python's stdlib is great, but I've found that I keep rewriting certain idioms
and utlity functions for multiple projects.  I'm collecting the best here.
"""


def chunk(xs, size):
    """Cuts a sequence `xs` into chunks of length `size`.

    Idiom taken from the [Python standard
    docs](https://docs.python.org/2/library/functions.html#zip).

    (seq(X), int) -> [tuple(X)]
    """
    return zip(* [iter(xs)] * size)
