#!/usr/bin/python

"""My list"""


class MyList(list):
    """prints the list, but sorted"""

    def print_sorted(self):
        print(sorted(self))
