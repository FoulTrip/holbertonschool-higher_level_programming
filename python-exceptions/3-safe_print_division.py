#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result is not None:
            if isinstance(result, int):
                print("Inside result: {:f}".format(result))
            else:
                print("Inside result: {:f}".format(int(result)))
        else:
            print("Inside result: {:f}".format(result))
        return result
