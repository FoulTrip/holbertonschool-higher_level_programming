#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix:
        for values in matrix:
            i = 1
            lenght = len(values)

            for value in values:
                if i == lenght:
                    print("{:d}".format(value), end="")
                else:
                    print("{:d}".format(value), end=" ")
                i += 1

            print()
