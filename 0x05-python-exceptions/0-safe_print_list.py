#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    list_number = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end="")
            list_number += 1
        except IndexError:
            break
    print("")
    return (list_number)
