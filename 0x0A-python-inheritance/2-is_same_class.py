#!/usr/bin/python3
"""2-is_same_class defines a function to compare the instance of a class"""


def is_same_class(obj, a_class):
    return isinstance(obj, a_class) and type(obj) == a_class
