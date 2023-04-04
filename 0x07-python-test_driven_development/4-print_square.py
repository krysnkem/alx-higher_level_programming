#!/usr/bin/python3
"""
The ``4-print_square`` module
It has one function that prints squares
"""


def print_square(size):
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) != int:
        raise TypeError("size must be an integer")
    i = 0
    for j in range(size):
        for k in range(size):
            print("#", end="")
        print("")
