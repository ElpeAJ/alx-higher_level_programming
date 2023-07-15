#!/usr/bin/python3

def max_integer(my_list=[]):
    count = 0
    for i in my_list:
        count += 0
    for i in range(count):
        my_list[i] = int(my_list[i])
    max_no = my_list[0]
    for i in my_list:
        if i > max_no:
            max_no = i
        if len(my_list) == 0:
            return (None)
