#!/usr/bin/python3
"""
    Defines an class called BaseGeometry
"""


class BaseGeometry:
    """ geometry class"""
    pass

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
