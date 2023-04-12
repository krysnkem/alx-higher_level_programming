#!/usr/bin/python3
"""0-lookup module contains lookup()"""


def lookup(obj):
    """lists available attribute and methods of an object"""
    return list(dir(obj))
