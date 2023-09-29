#!/usr/bin/python3
for number in range(0, 9):
    for digit in range(number + 1, 10):
        if number < 9:
            print("{:d}{:d}, ".format(number, digit), end="")
        else:
            print("{:d}{:d}".format(number, digit))