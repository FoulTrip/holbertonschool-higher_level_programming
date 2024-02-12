#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    # operación de diferencia simétrica (^):
    # obtiene los elementos presentes en un conjunto pero no en ambos
    diff = set_1 ^ set_2
    return diff
