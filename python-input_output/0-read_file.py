#!/usr/bin/python3

"""
This script defines a function 'read_file' that reads and prints the contents of a file.
"""


def read_file(filename=""):
    """
    Reads the contents of a file and prints them.

    Parameters:
    - filename: The name of the file to read. Defaults to an empty string.

    Returns: None
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
