#!/usr/bin/python3
"""Module that defines MyInt."""


class MyInt(int):
    """A rebel integer with inverted == and != operators."""

    def __eq__(self, other):
        """Invert equality."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Invert inequality."""
        return super().__eq__(other)
