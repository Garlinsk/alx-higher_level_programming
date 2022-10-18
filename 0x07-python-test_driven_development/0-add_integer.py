#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Float arguments are typecasted to ints before addition is performed.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if (type(a) is not [int, float]):
        raise TypeError("a must be an integer")
    if (type(b) is not [int,float]):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
