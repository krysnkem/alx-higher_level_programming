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
    """Rectangle class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Instanciates the BaseGeometry class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
        BaseGeometry.__init__(self)

    def area(self):
        """returns the area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns the string form of this rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class inherits from Rectangle class"""

    def __init__(self, size):
        """instanciates the Squqre class"""
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def __str__(self):
        """Returns the string form of this square"""
        return "[Square] {}/{}".format(self.__size, self.__size)
