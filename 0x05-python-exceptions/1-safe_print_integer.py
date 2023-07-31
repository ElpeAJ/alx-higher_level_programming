#!/usr/bin/python3

def safe_print_integer(value):
    while value:
        try:
            print("{:d}".format(value))
            break
            return True
        except ValueError:
            return False
