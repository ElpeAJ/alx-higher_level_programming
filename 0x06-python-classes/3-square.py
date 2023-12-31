#!/usr/bin/python3

"""
Define a class named Square
"""


class Square:
    """
    Define a class named Square
    """

    def __init__(self, size=0):
        """
        Initialize square
        """

        if (type(size) is int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Returns the area for a square
        """

        return (self.__size ** 2)
