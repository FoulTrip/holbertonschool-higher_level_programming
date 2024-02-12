#!/usr/bin/python3


def uniq_add(my_list=[]):
    result = 0
    # Elimino los duplicados
    conjunt = set(my_list)
    newList = list(conjunt)
    for number in newList:
        result += number
    return result
