#!/usr/bin/python3
"""
Function that returns True if and object is an instance
of a class that inherited from the specified class;
otherwise False
"""


def inherits_from(obj, a_class):
    """
    Determine whether the given object is an
    instance of the given type directly or
    indirectly

    Parameters
    obj : The instance variable
    a_class : type to be compared against

    Return : True if the object is an instance
    of a class that inherited from the specified class
    otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
