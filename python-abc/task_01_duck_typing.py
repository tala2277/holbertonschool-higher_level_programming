#!/usr/bin/env python3
"""Module that demonstrates abstract classes and duck typing."""

from abc import ABC, abstractmethod
import math


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
    """Circle shape."""

    def __init__(self, radius):
        """Initialize a circle."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        """Initialize a rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    """Print the area and perimeter of a shape."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
