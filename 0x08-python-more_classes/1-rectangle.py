#!/usr/bin/python3
"""``1-rectangle`` defines a rectangle class with and height attributes"""


class Rectangle:
    """Rectangle class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the class"""
        if width:
            self.width = width
        else:
            self.width = 0
        if height:
            self.height = height
        else:
            self.height = 0

    @property
    def width(self):
        """Retreives the width"""
        return self.__width

    @width.setter
    def width(self, value):
        "Sets the width property with a value"
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retreives the width"""
        return self.__height

    @height.setter
    def height(self, value):
        "Sets the height property with a value"
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
