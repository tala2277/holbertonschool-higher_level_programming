#!/usr/bin/python3
"""Module that defines a square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a square."""
        self.size = size

    @property
    def size(self):
        """Get the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __lt__(self, other):
        """Less than comparison."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparison."""
        return self.area() <= other.area()

    def __eq__(self, other):
        """Equal comparison."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Not equal comparison."""
        return self.area() != other.area()

    def __gt__(self, other):
        """Greater than comparison."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparison."""
        return self.area() >= other.area()
