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

    def validate(self, name, value):
        """
        Validates methods and attributes.

        Parameters
        name : str
        value : int

        Raises
        TypeError
            When the value is not int
        ValueError
            When the value given is 0 or less and the name
            is width or height. And also when the given
            value is a negative value and the name is x or y.
        """
        if (type(value) is not int):
            raise TypeError("{} must be an integer".format(name))
        if (name in ("width", "height")):
            if (value <= 0):
                raise ValueError("{} must be > 0".format(name))
        elif (name in ("x", "y")):
            if (value < 0):
                raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """ Returns width of rectangle """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Sets width of rectangle

        Parameters
        value : int
        """
        self.validate("width", value)
        self.__width = value

    @property
    def height(self):
        """ Returns height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height for the rectangle

        Parameters
        value : integer
        """
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """ Returns the x axis """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Set the x axis for the rectangle

        Parameters
        value : integer
        """
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """ Return the y axis """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Set the y axis for the rectangle

        Parameters
        value : integer
        """
        self.validate("y", value)
        self.__y = value
