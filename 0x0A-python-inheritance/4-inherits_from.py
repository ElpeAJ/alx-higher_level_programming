#!/usr/bin/python3
"""
Function that returns True if and object is an instance
of a class that inherited from the specified class;
otherwise False
"""


def inherits_from(obj, a_class):
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
