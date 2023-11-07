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
