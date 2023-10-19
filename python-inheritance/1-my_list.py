#!/usr/bin/python3

"""My list"""


class MyList(list):
    """prints the list, but sorted"""

    def print_sorted(self):
        """Print a list in sorted ascending order."""
        print(sorted(self))
