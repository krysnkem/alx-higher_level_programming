#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list != None:
        list_cpy = my_list.copy()
        list_cpy.reverse()
        for item in list_cpy:
            print("{:d}".format(item))
