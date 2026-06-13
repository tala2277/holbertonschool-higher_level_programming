#!/usr/bin/python3
"""Module that multiplies two matrices using NumPy."""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy."""
    return numpy.matrix(m_a) * numpy.matrix(m_b)
