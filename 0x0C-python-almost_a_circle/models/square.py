#!/usr/bin/python3
""" This module defines the Square blueprint """
from .rectangle import Rectangle


class Square(Rectangle):
    """ Represents the square shape """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize an instance of a square

        Parameters
        size : int
        x : int, optional
        y : int, optional
        """
        super().__init__(id=id, x=x, y=y, width=size, height=size)

    def __str__(self):
        """
        Returns the str representation of the square.
        """
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width, self.height))

        @property
    def size(self):
        """ Returns size of square """
        return (self.width)

    @size.setter
    def size(self, value):
        """
        Sets the size of the square

        Parameters
        value : int
            The size of square
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update square attributes

        Parameters
        args : tuple
        kwargs : dictionary
        """
        if (len(args) > 0 and type(args[0]) is int):
            if (len(args) == 1):
                self.id, = args
            elif (len(args) == 2):
                self.id, self.size = args
            elif (len(args) == 3):
                self.id, self.size, self.x = args
            else:
                self.id, self.size, self.x, self.y = args
        else:
            self.id = kwargs.get("id") if kwargs.get("id") \
                    is not None else self.id
            self.size = kwargs.get("size") if kwargs.get("size") \
                    is not None else self.size
            self.x = kwargs.get("x") if kwargs.get("x") \
                    is not None else self.x
            self.y = kwargs.get("y") if kwargs.get("y") \
                    is not None else self.y

    def to_dictionary(self):
        """
        Returns dictionary representation """
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "size": self.width
                }
