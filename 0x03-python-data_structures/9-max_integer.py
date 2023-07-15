#!/usr/bin/python3

def max_integer(my_list=[]):
    my_numbers_list = my_list.split(",")

    count = 0
    for i in my_list:
        count += 0
    for i in range(count):
        my_numbers_list[i] = int(my_numbers_list[i])
    max_no = my_numbers_list[0]
    for i in my_numbers_list:
        if i > max_no:
            max_no = i
        if len(my_numbers_list) == 0:
            return (None)
