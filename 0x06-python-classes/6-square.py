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

        Parameters
        size : int, optional
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

        if (type(value) is int):
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value
        else:
            raise TypeError("size must be an integer")

    def my_print(self):
        """prints in stdout the square with char #"""

        if self.__size != 0:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
