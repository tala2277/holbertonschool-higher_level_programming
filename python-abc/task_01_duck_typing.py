#!/usr/bin/env python3
"""Module for shapes and duck typing."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract shape."""

    @abstractmethod
    def area(self):
        """Return area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter."""
        pass


class Circle(Shape):
    """Circle."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (abs(self.radius) ** 2)

    def perimeter(self):
        return 2 * pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """Print shape information."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
