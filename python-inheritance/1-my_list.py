#!/usr/bin/python3
"""This module defines a class MyList."""


class MyList(list):
    """This class inherits from list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))
