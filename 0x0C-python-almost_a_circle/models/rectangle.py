#!/usr/bin/python3
""" This module defines the Rectangle blueprint """
from .base import Base


class Rectangle(Base):
    """ Reps the rectangle blueprint """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize instance of rectangle

        Parameters
        width : int
        height : int
        x : int, optional
        y : int, optional
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
            When the value is 0 or < &  name
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
        Sets height of rectangle

        Parameters
        value : int
        """
        self.validate("height", value)
        self.__height = value

    @property
    def x(self):
        """ Returns x axis of rectangle """
        return (self.__x)

    @x.setter
    def x(self, value):
        """
        Sets the x axis of the rectangle

        Parameters
        value : int
            The x axis for the rectangle
        """
        self.validate("x", value)
        self.__x = value

    @property
    def y(self):
        """ Returns the y axis of rectangle """
        return (self.__y)

    @y.setter
    def y(self, value):
        """
        Sets the y axis of rectangle

        Parameters
        value : int
            The y axis for the rectangle
        """
        self.validate("y", value)
        self.__y = value

    def area(self):
        """ Returns area of the rectangle """
        return (self.width * self.height)

    def __str__(self):
        """
        Returns string representation of the rectangle.
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
            self.x, self.y, self.width, self.height))

        def to_dictionary(self):
            """
        Returns dictionary representation for instance
        of a rectangle.
        """
        return {
                "x": self.x,
                "y": self.y,
                "id": self.id,
                "width": self.width, "height": self.height
                }
