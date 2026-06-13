#!/usr/bin/python3
"""Module that contains a function for adding two integers.

This module provides the add_integer function.
The function adds two integers and returns the result.
"""


def add_integer(a, b=98):
    """Add two integers.

    Floats are cast to integers before addition.
    Raises TypeError if a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float) and a != a:
        raise TypeError("a must be an integer")

    if isinstance(b, float) and b != b:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
