#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a_first = tuple_a[0] if len(tuple_a) > 0 else 0
    a_second = tuple_a[1] if len(tuple_a) > 1 else 0
    b_first = tuple_b[0] if len(tuple_b) > 0 else 0
    b_second = tuple_b[1] if len(tuple_b) > 1 else 0

    fValue = a_first + b_first
    sValue = a_second + b_second

    new_tuple = (fValue, sValue)
    return new_tuple


tiple_a = (1, 4, 7, 4, 3)
tiple_b = (5, 2, 9, 0, 3)
print(add_tuple(tiple_a, tiple_b))