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
    new_matrix = []
    new_list = []
    if not matrix:
        raise TypeError(list_error)
    if type(div) not in (int, float):
        raise TypeError(div_int_error)
    if div == 0:
        raise ZeroDivisionError(div_zero_error)
    longitud = len(matrix[0])
    for lista in matrix:
        if not isinstance(lista, list):
            raise TypeError(list_error)
        if len(lista) != longitud:
            raise TypeError(len_error)
        for item in lista:
            if not isinstance(item, (int, float)):
                raise TypeError(list_error)
            num = item / div
            new_list.append(round(num, 2))
        new_matrix.append(new_list)
        new_list = []
    return new_matrix


matrix = [[1.5, 2.5, 3.5], [4.5, 5.5, 6.5]]
div = 0.5
print(matrix_divided(matrix, div))