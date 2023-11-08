#!/usr/bin/python3
"""
Funtion returns the dictionary description with simple data
structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns dictionary for given object.

    Parameters
    obj : The given object

    Return : The dictionary of attributes.
    """
    obj_dict = obj.__dict__
    return (obj_dict)
