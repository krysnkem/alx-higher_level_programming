#!/usr/bin/python3
"""
    Defines an class called BaseGeometry
    and another called Rectangle that inherits from BaseGemetry
    class
"""


class BaseGeometry:
    """ geometry class"""

    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        BaseGeometry.__init__(self)
