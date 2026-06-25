#!/usr/bin/env python3
"""Module that demonstrates abstract classes and duck typing."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initialize a circle."""
        self.radius = radius

    def area(self):
        """Return the area."""
        return pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Return the perimeter."""
        return 2 * pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize a rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area."""
        return abs(self.width * self.height)

    def perimeter(self):
        """Return the perimeter."""
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """Print shape information."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
