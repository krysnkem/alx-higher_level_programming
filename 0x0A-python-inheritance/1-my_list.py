#!/usr/bin/python3
"""1-my_list module defines MyList class"""


class MyList(list):

    def print_sorted(self):
        print(sorted(self))
