#!/usr/bin/python3

"""Solution to task 3"""


class Square:
    """Defines a square with a size"""
    def __init__(self, size=0):
        """initializes square with private instance attribute called size"""
        if not size:
            self.__size = 0
        else:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        return self.__size * self.__size
