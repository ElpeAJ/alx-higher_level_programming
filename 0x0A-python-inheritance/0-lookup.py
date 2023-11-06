#!/usr/bin/python3
"""
The funtiong lookup returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods
    for a given object
    Parameters:  obj
    """
    return (dir(obj))
