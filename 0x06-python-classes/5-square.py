#!/usr/bin/python3

"""Solution to task 3"""


class Square:

    """Defines a square with a size"""
    def __init__(self, size=0):
        """initializes square with private instance attribute called size"""
        if not size:
            self.__size = 0
        else:
            self.size = size

    @property
    def size(self):
        """gets size and returns it to the caller"""
        return self.__size

    @size.setter
    def size(self, value):
        """checks and sets the value to size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """get the area of the square"""
        return self.__size * self.__size

    def my_print(self):
        if self.size > 0:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")

                print()
        else:
            print()
