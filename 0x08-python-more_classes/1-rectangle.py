#!/usr/bin/python3

"""Rectangle class definition"""


class Rectangle:
    """Defines a rectangular shape"""

    def __init__(self, width=0, height=0):
        """Instantiation with option width and height
        Arguments:
            width: integer and by default, 0
            height: integer and by defaul, 0
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve or set the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle"""
        if (type(value) is int):
            if (value < 0):
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Retrieve or set width of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle"""
        if (type(value) is int):
            if (value < 0):
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")
