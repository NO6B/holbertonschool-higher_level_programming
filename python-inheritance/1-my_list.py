#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """class MyList that inherits from list """
    def print_sorted(self):
        """rint the list in ascending order"""
        print(sorted(self))
