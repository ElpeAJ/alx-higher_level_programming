#!/usr/bin/python3
"""
A function to determine whether an
instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Is the given object is an
    exact instance of the given type?

    Parameters
    obj : object
    a_class : type

    Return : True if ``object`` is exactly
    an instance of ``a_class`` otherwise False.
    """
    return (type(obj) in (a_class, ))
