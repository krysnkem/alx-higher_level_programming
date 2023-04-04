#!/usr/bin/python3
"""
3-say_my_name

prints a sentence using first name and last name
"""

def say_my_name(first_name, last_name=""):
    """
    prints a sentence with ``first_name`` and ``last_name``
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
