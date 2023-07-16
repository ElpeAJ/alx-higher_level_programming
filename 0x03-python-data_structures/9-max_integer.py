#!/usr/bin/python3

def max_integer(my_list=[]):
    max_no = 0

    if (my_list):
        for i in my_list:
            if (i >= max_no):
                max_no = i
        return (max_no)
    return (None)
