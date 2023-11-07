#!/usr/bin/python3
"""
Define BaseGeometry class
"""


class BaseGeometry:
    """
    class defined
    """
    def area(self):
        """
        Returns area
        """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        validates value
        """
        if type(value) != "integer":
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0")
