#!/usr/bin/python3


def islower(c):
    i = ord(c)
    if i in range(97, 122, 1):
#        chr(i)
        return (True)
#    elif i in range(65, 91, 1):
#        chr(i)
#        return (False)
    else:
        return (False)
