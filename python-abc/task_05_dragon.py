#!/usr/bin/python3
"""Dragon module."""


class SwimMixin:
    """Mixin that adds swimming ability."""

    def swim(self):
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability."""

    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class."""

    def roar(self):
        print("The dragon roars!")
