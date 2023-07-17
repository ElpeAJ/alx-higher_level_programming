#!/usr/bin/python3


def element_at(my_list, idx):
    my_list_length = len(my_list) - 1
    if (idx < 0 or idx > my_list_length):
        return None
#    if idx > my_list_length:
#       return None
    else:
        return my_list[idx]
