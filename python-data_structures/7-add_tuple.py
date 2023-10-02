#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    fValue = tuple_a[0] + tuple_b[0]
    sValue = tuple_a[1] + tuple_b[1]
    new_tuple = (fValue, sValue)
    return new_tuple
