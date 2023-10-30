#!/usr/bin/python3

"""Rectangle class definition"""


class Rectangle:
    """Defines a rectangular shape"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with option width and height
        Arguments:
            width: integer and by default, 0
            height: integer and by defaul, 0
        """

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    def __del__(self):
        """Print message when an instance of rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @property
    def width(self):
        """Retrieve or set the width of rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle"""
        if (type(value) is int):
            if (value < 0):
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Retrieve or set width of rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle"""
        if (type(value) is int):
            if (value < 0):
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def perimeter(self):
        """Return perimeter of rectangle."""
        perimeter = 2 * (self.__width + self.__height)
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return perimeter

    def area(self):
        """Return area of rectangle."""
        area = self.__width * self.__height
        return area

    def __str__(self):
        """Returns string representation of rectangle"""

        object_string = ""

        if (self.__width == 0 or self.__height == 0):
            return object_string
        for r in range(0, self.__height):
            for c in range(0, self.__width):
                object_string += "#"
            if ((r == self.__height - 1) and (c == self.__width - 1)):
                break
            object_string += "\n"

        return object_string

    def __repr__(self):
        """Returns string representation of rectangle"""

        return (f"Rectangle({self.__width}, {self.__height})")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the biggest rectangle based on the area after
        comparing two instances of a rectangle

        Raises also: TypeError
        When either of the instances are not of type Rectangle.
        """

        if (type(rect_2) is Rectangle):
            if (type(rect_1) is Rectangle):
                if (rect_1.area() < rect_2.area()):
                    return rect_2
                return rect_1
            else:
                raise TypeError("rect_1 must be an instance of Rectangle")
        else:
            raise TypeError("rect_2 must be an instance of Rectangle")

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""

        rectangle2 = Rectangle(width=size, height=size)
        return rectangle2

