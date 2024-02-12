#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dicc = {}
    for key, value in a_dictionary.items():
        new_dicc[key] = value * 2
    return new_dicc
