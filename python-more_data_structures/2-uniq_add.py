#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    # Se convierte a conjunto ( elimina los duplicados )
    conjunt = set(my_list)
    # Se vuelve a convertir a lista
    newList = list(conjunt)
    for number in newList:
        result += number
    return result
