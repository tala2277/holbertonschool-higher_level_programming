#!/usr/bin/python3
"""Module that multiplies matrices using NumPy."""

import numpy


def lazy_matrix_mul(m_a, m_b):
    """Multiply 2 matrices using NumPy."""
    return numpy.matrix(m_a) * numpy.matrix(m_b)
