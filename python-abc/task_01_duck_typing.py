#!/usr/bin/env python3
"""Shape abstract class, Circle, Rectangle and duck typing."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """Return the perimeter."""
        raise NotImplementedError


class Circle(Shape):
    """Circle implementation."""

    def __init__(self, radius):
        """Initialize circle."""
        self.radius = radius

    def area(self):
        """Return area."""
        return pi * (self.radius * self.radius if self.radius >= 0
                     else (-self.radius) * (-self.radius))

    def perimeter(self):
        """Return perimeter."""
        return 2 * pi * (self.radius if self.radius >= 0 else -self.radius)


class Rectangle(Shape):
    """Rectangle implementation."""

    def __init__(self, width, height):
        """Initialize rectangle."""
        self.width = width
        self.height = height

    def area(self):
        """Return area."""
        area = self.width * self.height
        return area if area >= 0 else -area

    def perimeter(self):
        """Return perimeter."""
        w = self.width if self.width >= 0 else -self.width
        h = self.height if self.height >= 0 else -self.height
        return 2 * (w + h)


def shape_info(shape):
    """Print shape information."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
