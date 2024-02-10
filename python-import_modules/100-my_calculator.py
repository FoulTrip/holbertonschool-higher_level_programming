#!/usr/bin/python3

from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

    a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

    if not (a.isdigit() or (a[1:].isdigit() and a[0] == "-")):
        print("Error: Invalid input for <a>. Please enter a valid integer.")
        exit(1)

    if not (b.isdigit() or (b[1:].isdigit() and b[0] == "-")):
        print("Error: Invalid input for <b>. Please enter a valid integer.")
        exit(1)

    a, b = int(a), int(b)

    if operator not in ["+", "-", "*", "/"]:
        print("Error: Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if operator == "/" and b == 0:
        print("Error: Division by zero.")
        exit(1)

    result = {"+": add, "-": sub, "*": mul, "/": div}[operator](a, b)

    print("{} {} {} = {}".format(a, operator, b, result))
