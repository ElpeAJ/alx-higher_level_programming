#!/usr/bin/python3
"""a class MyInt that inherits from int"""


class MyInt(int):
    """int class"""
    def __eq__(self, other_value):
        """ """
        return (self.real != other_value)

    def __ne__(self, other_value):
        """ """
        return (self.real == other_value)
