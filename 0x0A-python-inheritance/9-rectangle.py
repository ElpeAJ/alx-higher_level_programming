#!/usr/bin/python3
"""
Define Rectangle class
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is the geometry shape for the rectangle
    """
    def __init__(self, width, height):
        """
        Initialize instance of a rectangle.

        Parameters
        width : int
        height : int
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def areaa(self):
        """ Return the area of the rectangle"""
        return (self.__height * self.__width)
    def __str__(self):
        """
        Return str representation of object
        """
        return("[{}] {}/{}" .format(type(self).__name__,
            self.__width, self.__height))
