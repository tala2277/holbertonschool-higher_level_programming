#!/usr/bin/python3
"""Module that contains a function for adding two integers.

This module provides the add_integer function.
The function adds two integers and returns the result.
"""


def add_integer(a, b=98):
    """Add two integers.

    Floats are cast to integers before addition.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        if a != a or a in (float('inf'), float('-inf')):
            raise TypeError("a must be an integer")

    if isinstance(b, float):
        if b != b or b in (float('inf'), float('-inf')):
            raise TypeError("b must be an integer")

    return int(a) + int(b)
