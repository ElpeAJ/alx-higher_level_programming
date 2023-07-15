#!/usr/bin/python3

def element_at(my_list, idx):
    count = 0
    for i in my_list:
        count += 1
    for i in count:
        if idx < 0:
            return (None)
        if idx > range(len(my_list)):
            return (None)
        return (my_list[idx])
