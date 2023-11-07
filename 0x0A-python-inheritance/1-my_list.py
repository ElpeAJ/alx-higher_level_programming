#!/usr/bin/python3
"""
Function that defines a customized List
"""


class MyList(list):
    """
    Create custom list from the list type
    """

    def print_sorted(self):
        """
        Create copy of the actual list
        and print the elements
        in the sorted increasing order.
        """
        cloned_list = self.copy()
        cloned_list.sort()
        print(cloned_list)
