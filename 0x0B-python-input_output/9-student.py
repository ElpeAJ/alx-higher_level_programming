#!/usr/bin/python3
""" Define Student class """


class Student:
    """ A class for a student instance """
    def __init__(self, first_name, last_name,  age):
        """
        Initialize student instance.

        Parameters
        first_name : string
        last_name : string
        age : integer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Returns a dictionary of all attributes of
        a student instance
        """
        return (self.__dict__)
