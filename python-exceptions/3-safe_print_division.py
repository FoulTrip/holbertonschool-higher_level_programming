#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result is not None:
            if isinstance(result, int):
                print("Inside result: {:d}".format(result))
            else:
                print("Inside result: {:d}".format(int(result)))
        else:
            print("Inside result: {}".format(result))
        return result
