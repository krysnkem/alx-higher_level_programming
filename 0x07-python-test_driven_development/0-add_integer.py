#!/usr/bin/python3
"""
This is the "0-add_integer" module

The 0-add_integer module supplies one function, add_integer().
"""


def add_integer(a, b=98):
    """
        This function adds two integers.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    calculation = int(a) + int(b)
    return calculation
