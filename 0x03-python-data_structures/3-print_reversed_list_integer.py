#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for idx in reversed(range(len(my_list))):
        print("{:d}".format(my_list[idx]))
