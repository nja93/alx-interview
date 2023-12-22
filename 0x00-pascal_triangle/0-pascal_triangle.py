#!/usr/bin/python3
"""
this odule returns a list of list of integers
representing the Pascal's triangle of n.
"""


def pascal_triangle(n):
    """Pascals triangle of n
    Args:
      n (int): height of triangle
    Returns:
      list of lists of integers representing the Pascal triangle of n
    """
    def factorial(n):
        if n <= 1:
            return 1
        return n * factorial(n - 1)

    def comb(m, n):
        return factorial(m) // (factorial(n) * factorial(m - n))

    if n <= 0:
        return []

    return [[comb(i, j) for j in range(i + 1)] for i in range(n)]
