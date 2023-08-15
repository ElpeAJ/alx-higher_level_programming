#!/usr/bin/python3

""" a function that returns True if the
object is exactly an instance of the specified
class ; otherwise False"""


def is_same_class(obj, a_class):
    """ returns True if object is exactly
    an instance of the class"""
    if type(obj) is not a_class:
        return False
    return True
