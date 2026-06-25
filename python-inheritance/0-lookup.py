#!/usr/bin/python3
"""This module defines a function that returns the attributes and methods
available for an object."""


def lookup(obj):
    """Return the list of attributes and methods of an object."""
    return dir(obj)
