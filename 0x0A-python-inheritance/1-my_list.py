#!/usr/bin/python3
"""1-my_list module defines MyList class"""


class MyList(list):
    """a sub class of list"""

    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
