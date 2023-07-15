#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return list(my_list)
    if idx > len(my_list) - 1:
        return list(my_list)
    my_list[idx] = element
    return my_list
