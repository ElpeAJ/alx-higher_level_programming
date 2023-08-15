#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """Class Mylist that inherits from list"""

    def print_sorted(self):
        """public instance method that
         prints the list in asc order
        """
        print(sorted(self))
