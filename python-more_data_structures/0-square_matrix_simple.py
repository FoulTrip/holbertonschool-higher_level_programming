#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    result = []
    for values in matrix:
        squared = []
        for value in values:
            squared.append(value**2)
        result.append(squared)
    return result
