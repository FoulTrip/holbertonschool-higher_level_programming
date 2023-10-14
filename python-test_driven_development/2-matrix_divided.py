#!/usr/bin/python3

"""
    Divide a matrix
"""


def matrix_divided(matrix, div):
    """Returns a new matrix
    matrix must be a list of lists of integers or floats
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(isinstance(row, list) for row in matrix) or not all(
        isinstance(element, (int, float)) for row in matrix for element in row
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(element / div) for element in row] for row in matrix]
    return new_matrix
