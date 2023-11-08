#!/usr/bin/python3
"""Define Student class"""


class Student:
    """ A class for a student instance """
    def __init__(self, first_name, last_name,  age):
        """
        Initialize a student instance.

        Parameters
        first_name : string
        last_name : string
        age : integer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary of all attributes.
        """
        my_dict = dict()

        if (type(attrs) is not list):
            return (self.__dict__)

        for element in attrs:
            if (element in self.__dict__.keys()):
                my_dict.__setitem__(element, self.__dict__.get(element))

        return (my_dict)

    def reload_from_json(self, json):
        """
        Parameters
        json : dictionary
        """
        for key, value in json.items():
            if (hasattr(self, key)):
                self.__dict__[key] = value
