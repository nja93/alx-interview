#!/usr/bin/python3
"""Rotates 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """function that rotates a square 2D matrix clockwise
    """
    n = len(matrix)
    copy = [[None for _ in range(n)]
            for _ in range(n)]
    for i in range(n):
        for j in range(n):
            copy[j][n-1-i] = matrix[i][j]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = copy[i][j]
