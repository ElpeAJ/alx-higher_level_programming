#!/usr/bin/python3
""" This module defines Base class """


class Base:
    """
    The blueprint Base class for all the shapes

    __nb_objects : integer
        The number of instances created
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an instance of the Base class

        id : integer, optional
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
