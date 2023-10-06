#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    for i in range(list_length):
        try:
            a = my_list_1[i] if i < len(my_list_1) else 0
            b = my_list_2[i] if i < len(my_list_2) else 0

            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise TypeError("tipo incorrecto")

            if b == 0:
                raise ZeroDivisionError("división por 0")

            result = a / b
        except ZeroDivisionError:
            print("división por 0")
            result = 0
        except TypeError:
            print("tipo incorrecto")
            result = 0
        except IndexError:
            print("fuera de rango")
            result = 0
        finally:
            result_list.append(result)
    return result_list
