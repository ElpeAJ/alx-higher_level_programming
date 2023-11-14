#!/usr/bin/python3
""" This created module defines the Base class """


class Base:
    """
    The Base class for all the shapes

    __nb_objects : integer
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the class

        id : integer, optional
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
