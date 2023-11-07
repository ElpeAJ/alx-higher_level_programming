#!/usr/bin/python3
"""
Funtion that defines if an
object is an instance of the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Function: is_kind_of_class

    Parameters
    obj : object
        The instance variable of the class
    a_class : type
        The class type to be compared against

    Return : True if object is an instance
    instance of a_class otherwise False.
    """
    return (issubclass(type(obj), a_class))
