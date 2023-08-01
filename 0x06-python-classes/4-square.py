#!/usr/bin/python3

"""
Define a class named Square that defines a square
"""


class Square:
    """
    Define a class named Square that defines a square
    """

    def __init__(self, size=0):
        """
        Initialize square
        """
        self.size = size

    def area(self):
        """
        Returns the area for a square
        """

        return (self.__size ** 2)

    @property
    def size(self):
        """
        return size for the square
        """

        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set size of the square
        """

        if(type(size) is int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            self.__size = size
        else:
            raise TypeError("size must be an integer")
