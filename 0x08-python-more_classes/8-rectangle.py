#!/usr/bin/python3
"""``5-rectangle`` defines a rectangle class with and height attributes"""


class Rectangle:
    """Rectangle class that defines a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the class"""
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        string = ""
        for h in range(self.height):
            for w in range(self.width):
                string += "{}".format(self.print_symbol)
            if (h < self.height - 1):
                string += "\n"
        return string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        self.__class__.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        rect_1_area = rect_1.area()
        rect_2_area = rect_2.area()
        if rect_1_area > rect_2_area:
            return rect_1
        elif rect_1_area < rect_2_area:
            return rect_2
        else:
            return rect_1
