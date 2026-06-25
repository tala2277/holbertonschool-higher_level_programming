#!/usr/bin/python3
"""Shapes using abstract base classes."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return perimeter."""
        pass


class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        return math.pi * (abs(self.radius) ** 2)

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return abs(self.width) * abs(self.height)

    def perimeter(self):
        return 2 * (abs(self.width) + abs(self.height))


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
