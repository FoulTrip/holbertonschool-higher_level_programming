#!/usr/bin/python3

"""
    Divide a matrix
"""


def matrix_divided(matrix, div):
    """Divide a matrix by a number div"""
    list_error = "matrix must be a matrix (list of lists) of integers/floats"
    len_error = "Each row of the matrix must have the same size"
    div_int_error = "div must be a number"
    div_zero_error = "division by zero"

    if not all(isinstance(row, list) for row in matrix) or not all(
        isinstance(item, (int, float)) for row in matrix for item in row
    ):
        raise TypeError(list_error)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError(len_error)

    if not isinstance(div, (int, float)):
        raise TypeError(div_int_error)

    if div == 0:
        raise ZeroDivisionError(div_zero_error)

    new_matrix = [[round(item / div, 2) for item in row] for row in matrix]
    return new_matrix
